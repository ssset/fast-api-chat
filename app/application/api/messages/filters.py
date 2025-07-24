from pydantic import BaseModel

from infra.repositories.filters.messages import GetMessagesFilter as GetMessagesInfraFilters

class GetMessagesFilters(BaseModel):
    limit: int
    offset: int

    def to_infra(self):
        return GetMessagesInfraFilters(limit=self.limit, offset=self.offset)