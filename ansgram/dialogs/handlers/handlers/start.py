from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.filters.state import State
from aiogram.types import ErrorEvent, Message
from aiogram_dialog import DialogManager, ShowMode, StartMode

from ....services.repo import UserRepo
from ...dialogs.main_menu.sg import MainMenuSG
from ...dialogs.settings.sg import SettingsSG

start_router = Router()


@start_router.error()
@start_router.message(CommandStart())
async def start(event: ErrorEvent | Message, dialog_manager: DialogManager) -> None:
    repo = UserRepo(dialog_manager.middleware_data["session"])

    await dialog_manager.start(
        await get_state_by_reg(repo, get_tg_id(event)),
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.EDIT,
    )


async def get_state_by_reg(repo: UserRepo, tg_id: int) -> State:
    is_registered = await repo.get_by_tg_id(tg_id)

    if not is_registered:
        return SettingsSG.BEGIN

    return MainMenuSG.MAIN_MENU


def get_tg_id(event: ErrorEvent | Message) -> int:
    if isinstance(event, ErrorEvent):
        return event.update.callback_query.from_user.id  # type: ignore[union-attr]

    return event.from_user.id  # type: ignore[union-attr]
