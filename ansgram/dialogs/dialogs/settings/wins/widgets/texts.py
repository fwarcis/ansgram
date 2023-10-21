from aiogram_dialog.widgets.text import Const, Format

BEGIN_TEXT = Format("*Данные настроек*")
SUBJECTS_TO_HELP_TEXT = Const(
    "Предметы, с которыми вы можете помочь людям (не указывайте, если их нет)?"
)
SUBJECTS_TO_ASK_TEXT = Const(
    "Предметы, в которых вам нужна помощь (не указывайте, если их нет)?"
)
GRADE_TEXT = Const("Ваш класс?")
DESCRIPTION_TEXT = Const(
    """
    Ваша компетентность:

    •  Где вы учились и где сейчас учитесь?
    •  Какие сведения, говорящие о ваших знаниях вы можете предоставить?
    """
)
DESCRIPTION_PROOFS_TEXT = Const(
    """
    Файл-доказательство (в любом из форматов ниже)?

    Доступные форматы:
    •  MS PowerPoint (pps, ppsm, ppsx, ppt, pptm, pptx)
    •  Изображения (png, jpg, jpeg)
    •  Документы (pdf)
    """
)
