from typing import Any

from aiogram_dialog.widgets.kbd import Column, Radio

from ..items import ITEM_ID_GETTER
from .texts import CHECKED_TEXT, UNCHECKED_TEXT


def column_radio(id: str, items: list[tuple[int, Any]]) -> Column:
    return Column(
        Radio(
            checked_text=CHECKED_TEXT,
            unchecked_text=UNCHECKED_TEXT,
            items=items,
            item_id_getter=ITEM_ID_GETTER,
            id=id,
        )
    )
