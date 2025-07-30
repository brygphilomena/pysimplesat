from pysimplesat.endpoints.base.base_endpoint import SimpleSatEndpoint
from pysimplesat.endpoints.simplesat.ReportsIdEndpoint import ReportsIdEndpoint
from pysimplesat.interfaces import (
    IGettable,
    IPaginateable,
)
from pysimplesat.models.simplesat import Reports
from pysimplesat.responses.paginated_response import PaginatedResponse
from pysimplesat.types import (
    JSON,
    SimpleSatRequestParams,
)


class ReportsEndpoint(
    SimpleSatEndpoint,
    IGettable[Reports, SimpleSatRequestParams],
    IPaginateable[Reports, SimpleSatRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        SimpleSatEndpoint.__init__(self, client, "reports", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Reports)
        IPaginateable.__init__(self, Reports)

    def id(self, id: int) -> ReportsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ReportsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ReportsIdEndpoint: The initialized ReportsIdEndpoint object.
        """
        child = ReportsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: SimpleSatRequestParams | None = None,
    ) -> PaginatedResponse[Reports]:
        """
        Performs a GET request against the /reports endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Reports]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["limit"] = limit
        else:
            params = {"page": page, "limit": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Reports,
            self,
            "reports",
            page,
            limit,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: SimpleSatRequestParams | None = None,
    ) -> Reports:
        """
        Performs a GET request against the /reports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AuthInformation: The parsed response data.
        """
        return self._parse_many(
            Reports,
            super()._make_request("GET", data=data, params=params).json().get('reports', {}),
        )
