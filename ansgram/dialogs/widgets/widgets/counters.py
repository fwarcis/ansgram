from aiogram_dialog.widgets.kbd import Counter


def grade_counter(id: str) -> Counter:
    return Counter(default=7, min_value=7, max_value=12, id=id)
