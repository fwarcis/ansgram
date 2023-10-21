from operator import itemgetter

from ...models import Subjects

ITEM_ID_GETTER = itemgetter(0)
SUBJECTS_ITEMS = list((i, s.value) for i, s in zip(range(len(Subjects)), Subjects))
