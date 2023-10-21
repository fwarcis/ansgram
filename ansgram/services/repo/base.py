from sqlalchemy.ext.asyncio import AsyncSession

from ...models.orm import Entry


class Repo:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    def add(self, *entries: Entry) -> None:
        self._session.add_all(entries)

    async def get_by_primary_key_id(self, table: type[Entry], id: int) -> Entry | None:
        return await self._session.get(table, id)

    async def delete(self, entry: Entry) -> None:
        await self._session.delete(entry)
