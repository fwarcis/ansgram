from aiogram_dialog import Dialog

from .wins.wins import begin_win, categories_win, filters_win, grade_win, subjects_win

search_dialog = Dialog(categories_win, begin_win, filters_win, subjects_win, grade_win)
