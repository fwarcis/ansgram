from aiogram_dialog import Window

from ....widgets.widgets.btns import BACK
from ....widgets.widgets.navs import BACK_NEXT_NAV
from ..sg import SearchSG
from .widgets.btns.categories import (
    MY_ANSWERS_BTN,
    MY_QUESTIONS_BTN,
    PEOPLE_BTN,
    PEOPLE_QUESTIONS_BTN,
)
from .widgets.btns.filters import FILTERS_BTN, GRADES_BTN, SUBJECTS_BTN
from .widgets.inputs import KEYWORDS_INPUT
from .widgets.multiselects import SUBJECTS_MULTISELECT
from .widgets.texts import (
    BEGIN_TEXT,
    CATEGORIES_TEXT,
    FILTERS_TEXT,
    GRADES_TEXT,
    SUBJECTS_TEXT,
)

categories_win = Window(
    CATEGORIES_TEXT,
    MY_ANSWERS_BTN,
    MY_QUESTIONS_BTN,
    PEOPLE_BTN,
    PEOPLE_QUESTIONS_BTN,
    BACK_NEXT_NAV,
    state=SearchSG.CATEGORIES,
)

begin_win = Window(
    BEGIN_TEXT,
    BACK_NEXT_NAV,
    state=SearchSG.BEGIN,
)

filters_win = Window(
    FILTERS_TEXT,
    KEYWORDS_INPUT,
    GRADES_BTN,
    SUBJECTS_BTN,
    BACK,
    state=SearchSG.FILTERS,
)

subjects_win = Window(
    SUBJECTS_TEXT,
    SUBJECTS_MULTISELECT,
    FILTERS_BTN,
    state=SearchSG.SUBJECTS,
)

grade_win = Window(
    GRADES_TEXT,
    FILTERS_BTN,
    state=SearchSG.GRADES,
)
