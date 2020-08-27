from .abc import ABCAPI
from .response_validator import ABCResponseValidator, DEFAULT_RESPONSE_VALIDATORS
from vkbottle.http import ABCSessionManager, SessionManager, AiohttpClient
from vkbottle.exception_factory import ABCErrorHandler, ErrorHandler
import typing


APIRequest = typing.NamedTuple("APIRequest", [("method", str), ("data", dict)])


class API(ABCAPI):
    """ Default API instance
    Documentation: https://github.com/timoniq/vkbottle/tree/v3.0/docs/api/api.md
    """

    API_URL = "https://api.vk.com/method/"
    API_VERSION = "5.103"
    APIRequest = APIRequest

    def __init__(
        self,
        token: str,
        ignore_errors: bool = False,
        session_manager: typing.Optional[SessionManager] = None,
        error_handler: typing.Optional[ABCErrorHandler] = None,
    ):
        self.token = token
        self.ignore_errors = ignore_errors
        self.http: ABCSessionManager = session_manager or SessionManager(AiohttpClient)
        self.error_handler = error_handler or ErrorHandler(redirect_arguments=False)
        self.response_validators: typing.List[ABCResponseValidator] = DEFAULT_RESPONSE_VALIDATORS

    async def request(self, method: str, data: dict) -> dict:
        """ Makes a single request opening a session """
        async with self.http as session:
            response = await session.request_text(
                "POST",
                self.API_URL + method,
                data=data,
                params={"access_token": self.token, "v": self.API_VERSION},
            )
            return await self.validate_response(response)

    async def request_many(
        self, requests: typing.Iterable[APIRequest]
    ) -> typing.AsyncIterator[dict]:
        """ Makes many requests opening one session """
        async with self.http as session:
            for request in requests:
                response = await session.request_text(
                    "POST",
                    self.API_URL + request.method,
                    data=request.data,
                    params={"access_token": self.token, "v": self.API_VERSION},
                )
                yield await self.validate_response(response)

    async def validate_response(self, response: dict) -> typing.Union[dict, typing.NoReturn]:
        """ Validates response from VK,
        to change validations change API.response_validators (list of ResponseValidator's) """
        for validator in self.response_validators:
            response = await validator.validate(response)
        return response
