from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


class DbMiddleware(BaseMiddleware):
    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        super().__init__()
        self.pool = pool

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ):
        session: AsyncSession

        async with self.pool.begin() as session:
            data["session"] = session

            await handler(event, data)
