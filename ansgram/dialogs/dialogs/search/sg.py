from aiogram.filters.state import State, StatesGroup


class SearchSG(StatesGroup):
    CATEGORIES = State()
    BEGIN = State()
    FILTERS = State()
    KEYWORDS = State()
    SUBJECTS = State()
    GRADES = State()
