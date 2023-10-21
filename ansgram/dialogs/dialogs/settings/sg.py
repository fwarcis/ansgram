from aiogram.filters.state import State, StatesGroup


class SettingsSG(StatesGroup):
    BEGIN = State()
    SUBJECTS_TO_HELP = State()
    SUBJECTS_TO_ASK = State()
    GRADE = State()
    DESCRIPTION = State()
    DESCRIPTION_PROOFS = State()
