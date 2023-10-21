from aiogram_dialog import Window

from ....widgets.widgets.btns import BACK, NEXT
from ..sg import QuestionSG
from .widgets.btns import HEADER_BTN, TEXT_BTN
from .widgets.inputs import INPUT
from .widgets.text import BEGIN_TEXT

begin_win = Window(
    BEGIN_TEXT,
    INPUT,
    HEADER_BTN,
    TEXT_BTN,
    NEXT,
    BACK,
    state=QuestionSG.BEGIN,
)

subject_win = Window(
    ...,
    BACK,
    state=QuestionSG.SUBJECT,
)
