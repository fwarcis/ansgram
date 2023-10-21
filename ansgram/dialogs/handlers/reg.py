from aiogram import Dispatcher

from .handlers.start import start_router


def include_routers(dp: Dispatcher) -> None:
    dp.include_routers(start_router)
