from aiogram_dialog.widgets.kbd import Next
from aiogram_dialog.widgets.text import Const

MY_QUESTIONS_BTN_ID = "_"
MY_ANSWERS_BTN_ID = "_"
PEOPLE_QUESTIONS_BTN_ID = "_"
PEOPLE_BTN_ID = "_"

MY_QUESTIONS_BTN = Next(Const("Мои вопросы"), MY_QUESTIONS_BTN_ID)
MY_ANSWERS_BTN = Next(Const("Мои ответы"), MY_ANSWERS_BTN_ID)
PEOPLE_QUESTIONS_BTN = Next(Const("Вопросы людей"), PEOPLE_QUESTIONS_BTN_ID)
PEOPLE_BTN = Next(Const("Люди"), PEOPLE_BTN_ID)
