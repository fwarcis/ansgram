from aiogram_dialog import Window

from ..sg import MainMenuSG
from .widgets.btns import QUESTION_START, SEARCH_START, SETTINGS_START
from .widgets.texts import MAIN_MENU_TEXT

main_menu_win = Window(
    MAIN_MENU_TEXT,
    QUESTION_START,
    SEARCH_START,
    SETTINGS_START,
    state=MainMenuSG.MAIN_MENU,
)
