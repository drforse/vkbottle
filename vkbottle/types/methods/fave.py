# Generated with love
import typing
import enum
from vkbottle.types import responses
from .access import APIAccessibility
from .method import BaseMethod


class FaveAddArticle(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, url: str) -> responses.fave.AddArticle:
        """ fave.addArticle
        From Vk Docs: 
        Access from user token(s)
        :param url: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.addArticle", params, response_model=responses.fave.AddArticle
        )


class FaveAddLink(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, link: str) -> responses.fave.AddLink:
        """ fave.addLink
        From Vk Docs: Adds a link to user faves.
        Access from user token(s)
        :param link: Link URL.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.addLink", params, response_model=responses.fave.AddLink
        )


class FaveAddPage(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, user_id: int, group_id: int) -> responses.fave.AddPage:
        """ fave.addPage
        From Vk Docs: 
        Access from user token(s)
        :param user_id: 
        :param group_id: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.addPage", params, response_model=responses.fave.AddPage
        )


class FaveAddPost(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, owner_id: int, id: int, access_key: str
    ) -> responses.fave.AddPost:
        """ fave.addPost
        From Vk Docs: 
        Access from user token(s)
        :param owner_id: 
        :param id: 
        :param access_key: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.addPost", params, response_model=responses.fave.AddPost
        )


class FaveAddProduct(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, owner_id: int, id: int, access_key: str
    ) -> responses.fave.AddProduct:
        """ fave.addProduct
        From Vk Docs: 
        Access from user token(s)
        :param owner_id: 
        :param id: 
        :param access_key: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.addProduct", params, response_model=responses.fave.AddProduct
        )


class FaveAddTag(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, name: str) -> responses.fave.AddTag:
        """ fave.addTag
        From Vk Docs: 
        Access from user token(s)
        :param name: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.addTag", params, response_model=responses.fave.AddTag
        )


class FaveAddVideo(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, owner_id: int, id: int, access_key: str
    ) -> responses.fave.AddVideo:
        """ fave.addVideo
        From Vk Docs: 
        Access from user token(s)
        :param owner_id: 
        :param id: 
        :param access_key: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.addVideo", params, response_model=responses.fave.AddVideo
        )


class FaveEditTag(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, id: int, name: str) -> responses.fave.EditTag:
        """ fave.editTag
        From Vk Docs: 
        Access from user token(s)
        :param id: 
        :param name: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.editTag", params, response_model=responses.fave.EditTag
        )


class FaveGet(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        extended: bool,
        item_type: str,
        tag_id: int,
        offset: int,
        count: int,
        fields: str,
        is_from_snackbar: bool,
    ) -> responses.fave.Get:
        """ fave.get
        From Vk Docs: 
        Access from user token(s)
        :param extended: '1' — to return additional 'wall', 'profiles', and 'groups' fields. By default: '0'.
        :param item_type: 
        :param tag_id: Tag ID.
        :param offset: Offset needed to return a specific subset of users.
        :param count: Number of users to return.
        :param fields: 
        :param is_from_snackbar: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("fave.get", params, response_model=responses.fave.Get)


class FaveGetPages(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, offset: int, count: int, type: str, fields: typing.List, tag_id: int
    ) -> responses.fave.GetPages:
        """ fave.getPages
        From Vk Docs: 
        Access from user token(s)
        :param offset: 
        :param count: 
        :param type: 
        :param fields: 
        :param tag_id: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.getPages", params, response_model=responses.fave.GetPages
        )


class FaveGetTags(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self,) -> responses.fave.GetTags:
        """ fave.getTags
        From Vk Docs: 
        Access from user token(s)
        
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.getTags", params, response_model=responses.fave.GetTags
        )


class FaveMarkSeen(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self,) -> responses.fave.MarkSeen:
        """ fave.markSeen
        From Vk Docs: 
        Access from user token(s)
        
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.markSeen", params, response_model=responses.fave.MarkSeen
        )


class FaveRemoveArticle(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, owner_id: int, article_id: int
    ) -> responses.fave.RemoveArticle:
        """ fave.removeArticle
        From Vk Docs: 
        Access from user token(s)
        :param owner_id: 
        :param article_id: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.removeArticle", params, response_model=responses.fave.RemoveArticle
        )


class FaveRemoveLink(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, link_id: str, link: str) -> responses.fave.RemoveLink:
        """ fave.removeLink
        From Vk Docs: Removes link from the user's faves.
        Access from user token(s)
        :param link_id: Link ID (can be obtained by [vk.com/dev/faves.getLinks|faves.getLinks] method).
        :param link: Link URL
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.removeLink", params, response_model=responses.fave.RemoveLink
        )


class FaveRemovePage(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, user_id: int, group_id: int) -> responses.fave.RemovePage:
        """ fave.removePage
        From Vk Docs: 
        Access from user token(s)
        :param user_id: 
        :param group_id: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.removePage", params, response_model=responses.fave.RemovePage
        )


class FaveRemovePost(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, id: int) -> responses.fave.RemovePost:
        """ fave.removePost
        From Vk Docs: 
        Access from user token(s)
        :param owner_id: 
        :param id: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.removePost", params, response_model=responses.fave.RemovePost
        )


class FaveRemoveProduct(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, id: int) -> responses.fave.RemoveProduct:
        """ fave.removeProduct
        From Vk Docs: 
        Access from user token(s)
        :param owner_id: 
        :param id: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.removeProduct", params, response_model=responses.fave.RemoveProduct
        )


class FaveRemoveTag(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, id: int) -> responses.fave.RemoveTag:
        """ fave.removeTag
        From Vk Docs: 
        Access from user token(s)
        :param id: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.removeTag", params, response_model=responses.fave.RemoveTag
        )


class FaveReorderTags(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, ids: typing.List) -> responses.fave.ReorderTags:
        """ fave.reorderTags
        From Vk Docs: 
        Access from user token(s)
        :param ids: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.reorderTags", params, response_model=responses.fave.ReorderTags
        )


class FaveSetPageTags(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, user_id: int, group_id: int, tag_ids: typing.List
    ) -> responses.fave.SetPageTags:
        """ fave.setPageTags
        From Vk Docs: 
        Access from user token(s)
        :param user_id: 
        :param group_id: 
        :param tag_ids: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.setPageTags", params, response_model=responses.fave.SetPageTags
        )


class FaveSetTags(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        item_type: str,
        item_owner_id: int,
        item_id: int,
        tag_ids: typing.List,
        link_id: str,
        link_url: str,
    ) -> responses.fave.SetTags:
        """ fave.setTags
        From Vk Docs: 
        Access from user token(s)
        :param item_type: 
        :param item_owner_id: 
        :param item_id: 
        :param tag_ids: 
        :param link_id: 
        :param link_url: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.setTags", params, response_model=responses.fave.SetTags
        )


class FaveTrackPageInteraction(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, user_id: int, group_id: int
    ) -> responses.fave.TrackPageInteraction:
        """ fave.trackPageInteraction
        From Vk Docs: 
        Access from user token(s)
        :param user_id: 
        :param group_id: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "fave.trackPageInteraction",
            params,
            response_model=responses.fave.TrackPageInteraction,
        )


class Fave:
    def __init__(self, request):
        self.add_article = FaveAddArticle(request)
        self.add_link = FaveAddLink(request)
        self.add_page = FaveAddPage(request)
        self.add_post = FaveAddPost(request)
        self.add_product = FaveAddProduct(request)
        self.add_tag = FaveAddTag(request)
        self.add_video = FaveAddVideo(request)
        self.edit_tag = FaveEditTag(request)
        self.get = FaveGet(request)
        self.get_pages = FaveGetPages(request)
        self.get_tags = FaveGetTags(request)
        self.mark_seen = FaveMarkSeen(request)
        self.remove_article = FaveRemoveArticle(request)
        self.remove_link = FaveRemoveLink(request)
        self.remove_page = FaveRemovePage(request)
        self.remove_post = FaveRemovePost(request)
        self.remove_product = FaveRemoveProduct(request)
        self.remove_tag = FaveRemoveTag(request)
        self.reorder_tags = FaveReorderTags(request)
        self.set_page_tags = FaveSetPageTags(request)
        self.set_tags = FaveSetTags(request)
        self.track_page_interaction = FaveTrackPageInteraction(request)