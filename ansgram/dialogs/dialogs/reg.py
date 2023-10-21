from aiogram import Dispatcher

from .answer.dialog import answer_dialog
from .main_menu.dialog import main_menu_dialog
from .question.dialog import question_dialog
from .search.dialog import search_dialog
from .settings.dialog import settings_dialog


def include_dialogs(dp: Dispatcher) -> None:
    dp.include_routers(
        main_menu_dialog,
        settings_dialog,
        question_dialog,
        search_dialog,
        answer_dialog,
    )
