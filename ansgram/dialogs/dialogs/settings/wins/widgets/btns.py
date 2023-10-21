from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.text import Const

from ...sg import SettingsSG

SUBJECTS_TO_HELP_BTN_ID = "_"
SUBJECTS_TO_ASK_BTN_ID = "_"

SUBJECTS_TO_HELP_BTN = SwitchTo(
    Const("Предметы для получения помощи"),
    SUBJECTS_TO_HELP_BTN_ID,
    SettingsSG.SUBJECTS_TO_HELP,
)

SUBJECTS_TO_ASK_BTN = SwitchTo(
    Const("Предметы для оказания помощи"),
    SUBJECTS_TO_ASK_BTN_ID,
    SettingsSG.SUBJECTS_TO_ASK,
)
