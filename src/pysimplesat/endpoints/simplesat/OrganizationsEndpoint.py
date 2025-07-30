from pysimplesat.endpoints.base.base_endpoint import SimpleSatEndpoint
from pysimplesat.endpoints.simplesat.OrganizationsIdEndpoint import OrganizationsIdEndpoint
from pysimplesat.interfaces import (
    IGettable,
    IPaginateable,
)
from pysimplesat.models.simplesat import Organizations
from pysimplesat.responses.paginated_response import PaginatedResponse
from pysimplesat.types import (
    JSON,
    SimpleSatRequestParams,
)


class OrganizationsEndpoint(
    SimpleSatEndpoint,
    IGettable[Organizations, SimpleSatRequestParams],
    IPaginateable[Organizations, SimpleSatRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        SimpleSatEndpoint.__init__(self, client, "organizations", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Organizations)
        IPaginateable.__init__(self, Organizations)

    def id(self, id: int) -> OrganizationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized OrganizationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            OrganizationsIdEndpoint: The initialized OrganizationsIdEndpoint object.
        """
        child = OrganizationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: SimpleSatRequestParams | None = None,
    ) -> PaginatedResponse[Organizations]:
        """
        Performs a GET request against the /organizations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Organizations]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["limit"] = limit
        else:
            params = {"page": page, "limit": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Organizations,
            self,
            "organizations",
            page,
            limit,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: SimpleSatRequestParams | None = None,
    ) -> Organizations:
        """
        Performs a GET request against the /Organizations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AuthInformation: The parsed response data.
        """
        return self._parse_many(
            Organizations,
            super()._make_request("GET", data=data, params=params).json().get('organizations', {}),
        )
