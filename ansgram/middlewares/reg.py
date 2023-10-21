from aiogram import Dispatcher
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from .middlewares.db import DbMiddleware
from .middlewares.log import LogMiddleware


def reg_middlewares(dp: Dispatcher, sm: async_sessionmaker[AsyncSession]):
    dp.update.outer_middleware(DbMiddleware(sm))
    dp.update.outer_middleware(LogMiddleware())
