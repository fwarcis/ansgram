from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.text import Const

from ....sg import SearchSG

KEYWORDS_BTN_ID = "_"
SUBJECTS_BTN_ID = "_"
GRADES_BTN_ID = "_"
FILTERS_BTN_ID = "_"

SUBJECTS_BTN = SwitchTo(Const("Предметы"), SUBJECTS_BTN_ID, SearchSG.SUBJECTS)
GRADES_BTN = SwitchTo(Const("Классы"), GRADES_BTN_ID, SearchSG.GRADES)
FILTERS_BTN = SwitchTo(Const("Фильтры"), FILTERS_BTN_ID, SearchSG.FILTERS)
