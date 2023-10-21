import asyncio

import aiogram_dialog
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import (
    MemoryStorage,
)
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from .cfg import BotCfg, DbCfg, load_cfg
from .dialogs.dialogs.reg import include_dialogs
from .dialogs.handlers.reg import include_routers
from .middlewares.reg import reg_middlewares


async def run_bot() -> None:
    cfg = load_cfg("cfg.ini")
    bot, dp = init_bot(cfg.bot)
    sm = sessionmaker(cfg.db)
    reg_handling_objs(dp, sm)

    await bot.delete_webhook()
    await dp.start_polling(bot)


def init_bot(cfg: BotCfg) -> tuple[Bot, Dispatcher]:
    bot = Bot(cfg.token)
    dp = Dispatcher(storage=MemoryStorage())

    return bot, dp


def reg_handling_objs(dp: Dispatcher, sm: async_sessionmaker[AsyncSession]) -> None:
    reg_middlewares(dp, sm)
    include_routers(dp)
    include_dialogs(dp)

    aiogram_dialog.setup_dialogs(dp)


def sessionmaker(cfg: DbCfg) -> async_sessionmaker[AsyncSession]:
    db_engine = create_async_engine(cfg.path, echo=cfg.dbms.echo)

    return async_sessionmaker(db_engine, expire_on_commit=cfg.dbms.expire_on_commit)


def __main__():
    asyncio.run(run_bot())


if __name__ == "__main__":
    __main__()
