from pydantic import BaseModel

from infra.repositories.filters.messages import (
    GetMessagesFilter as GetMessagesInfraFilters,
    GetAllChatsFilters as GetAllChatsInfraFilters
)

class GetMessagesFilters(BaseModel):
    limit: int
    offset: int

    def to_infra(self):
        return GetMessagesInfraFilters(limit=self.limit, offset=self.offset)


class GetAllChatsFilters(BaseModel):
    limit: int
    offset: int

    def to_infra(self):
        return GetAllChatsInfraFilters(limit=self.limit, offset=self.offset)