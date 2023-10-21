from aiogram_dialog import Dialog

from .wins.wins import begin_win, subject_win

question_dialog = Dialog(begin_win, subject_win)
