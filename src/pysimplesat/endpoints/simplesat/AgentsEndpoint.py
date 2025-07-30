from pysimplesat.endpoints.base.base_endpoint import SimpleSatEndpoint
from pysimplesat.endpoints.simplesat.AgentsIdEndpoint import AgentsIdEndpoint
from pysimplesat.interfaces import (
    IGettable,
    IPaginateable,
)
from pysimplesat.models.simplesat import Agents
from pysimplesat.responses.paginated_response import PaginatedResponse
from pysimplesat.types import (
    JSON,
    SimpleSatRequestParams,
)


class AgentsEndpoint(
    SimpleSatEndpoint,
    IGettable[Agents, SimpleSatRequestParams],
    IPaginateable[Agents, SimpleSatRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        SimpleSatEndpoint.__init__(self, client, "agents", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Agents)
        IPaginateable.__init__(self, Agents)

    def id(self, id: int) -> AgentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized AgentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            AgentsIdEndpoint: The initialized AgentsIdEndpoint object.
        """
        child = AgentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: SimpleSatRequestParams | None = None,
    ) -> PaginatedResponse[Agents]:
        """
        Performs a GET request against the /agents endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Agents]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["limit"] = limit
        else:
            params = {"page": page, "limit": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Agents,
            self,
            "agents",
            page,
            limit,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: SimpleSatRequestParams | None = None,
    ) -> Agents:
        """
        Performs a GET request against the /agents endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AuthInformation: The parsed response data.
        """
        return self._parse_many(
            Agents,
            super()._make_request("GET", data=data, params=params).json().get('agents', {}),
        )
