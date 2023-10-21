from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from ....question.sg import QuestionSG
from ....search.sg import SearchSG
from ....settings.sg import SettingsSG

SETTINGS_START_ID = "_"
QUESTION_START_ID = "_"
SEARCH_START_ID = "_"

SETTINGS_START = Start(
    Const("Настройки"),
    id=SETTINGS_START_ID,
    state=SettingsSG.BEGIN,
)

QUESTION_START = Start(
    Const("Задать вопрос"),
    id=QUESTION_START_ID,
    state=QuestionSG.BEGIN,
)

SEARCH_START = Start(
    Const("Поиск"),
    id=SEARCH_START_ID,
    state=SearchSG.CATEGORIES,
)
