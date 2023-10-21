from aiogram_dialog import Window

from ....widgets.widgets.btns import BACK
from ..sg import SettingsSG
from .widgets.btns import SUBJECTS_TO_ASK_BTN, SUBJECTS_TO_HELP_BTN
from .widgets.counters import GRADE_COUNTER
from .widgets.inputs import DESCRIPTION_INPUT, DESCRIPTION_PROOFS_INPUT
from .widgets.multiselects import (
    SUBJECTS_TO_ASK_MULTISELECT,
    SUBJECTS_TO_HELP_MULTISELECT,
)
from .widgets.texts import (
    BEGIN_TEXT,
    DESCRIPTION_PROOFS_TEXT,
    DESCRIPTION_TEXT,
    GRADE_TEXT,
    SUBJECTS_TO_ASK_TEXT,
    SUBJECTS_TO_HELP_TEXT,
)

begin_win = Window(
    BEGIN_TEXT,
    SUBJECTS_TO_ASK_BTN,
    SUBJECTS_TO_HELP_BTN,
    BACK,
    state=SettingsSG.BEGIN,
)

subjects_to_help_win = Window(
    SUBJECTS_TO_HELP_TEXT,
    SUBJECTS_TO_HELP_MULTISELECT,
    BACK,
    state=SettingsSG.SUBJECTS_TO_ASK,
)

subjects_to_ask_win = Window(
    SUBJECTS_TO_ASK_TEXT,
    SUBJECTS_TO_ASK_MULTISELECT,
    BACK,
    state=SettingsSG.SUBJECTS_TO_HELP,
)

grade_win = Window(
    GRADE_TEXT,
    GRADE_COUNTER,
    BACK,
    state=SettingsSG.GRADE,
)

description_win = Window(
    DESCRIPTION_TEXT,
    DESCRIPTION_INPUT,
    BACK,
    state=SettingsSG.DESCRIPTION,
)

description_proofs_win = Window(
    DESCRIPTION_PROOFS_TEXT,
    DESCRIPTION_PROOFS_INPUT,
    BACK,
    state=SettingsSG.DESCRIPTION_PROOFS,
)
