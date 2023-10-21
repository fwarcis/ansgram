from aiogram_dialog import Dialog

from .wins.wins import (
    begin_win,
    description_proofs_win,
    description_win,
    grade_win,
    subjects_to_ask_win,
    subjects_to_help_win,
)

settings_dialog = Dialog(
    begin_win,
    subjects_to_help_win,
    subjects_to_ask_win,
    grade_win,
    description_win,
    description_proofs_win,
)
