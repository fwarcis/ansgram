from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

HEADER_BTN_ID = "_"
TEXT_BTN_ID = "_"
SUBJECT_BTN_ID = "_"

HEADER_BTN = Button(Const("Заголовок"), HEADER_BTN_ID, func)
TEXT_BTN = Button(Const("Текст"), TEXT_BTN_ID, func)
