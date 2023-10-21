from typing import Any

from aiogram_dialog.widgets.kbd import Column, Multiselect

from ..items import ITEM_ID_GETTER, SUBJECTS_ITEMS
from .texts import CHECKED_TEXT, UNCHECKED_TEXT


def column_multiselect(id: str, items: list[tuple[int, Any]]) -> Column:
    return Column(
        Multiselect(
            checked_text=CHECKED_TEXT,
            unchecked_text=UNCHECKED_TEXT,
            items=items,
            item_id_getter=ITEM_ID_GETTER,
            id=id,
        )
    )


def subjects_multiselect(id: str) -> Column:
    return column_multiselect(id, SUBJECTS_ITEMS)
