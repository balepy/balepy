from typing import Optional
from balepy.objects import HTTPMethod
from balepy.types import UserProfilePhotos
import balepy


class GetUserProfilePhotos:

    async def get_user_profile_photos(
            self: "balepy.Client",
            user_id: int,
            offset: Optional[int] = None,
            limit: Optional[int] = None
    ) -> UserProfilePhotos:
        params = {
            'user_id': user_id,
            'offset': offset,
            'limit': limit
        }
        response = await self.api.execute(name="getUserProfilePhotos", method=HTTPMethod.POST, data=params)
        return UserProfilePhotos(response)
