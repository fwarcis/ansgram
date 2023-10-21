from aiogram.filters.state import State, StatesGroup


class QuestionSG(StatesGroup):
    BEGIN = State()
    SUBJECT = State()
