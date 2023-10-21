from sqlalchemy import select

from ...models.orm.user import User
from . import Repo


class UserRepo(Repo):
    async def get_by_tg_id(self, id: int) -> User | None:
        return await self._session.scalar(select(User).where(User.tg_id == id))
