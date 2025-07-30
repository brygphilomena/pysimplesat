from pysimplesat.endpoints.base.base_endpoint import SimpleSatEndpoint
from pysimplesat.endpoints.simplesat.IncidentreportsIdEndpoint import IncidentreportsIdEndpoint
from pysimplesat.interfaces import (
    IGettable,
    IPaginateable,
)
from pysimplesat.models.simplesat import IncidentReports
from pysimplesat.responses.paginated_response import PaginatedResponse
from pysimplesat.types import (
    JSON,
    SimpleSatRequestParams,
)


class IncidentreportsEndpoint(
    SimpleSatEndpoint,
    IGettable[IncidentReports, SimpleSatRequestParams],
    IPaginateable[IncidentReports, SimpleSatRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        SimpleSatEndpoint.__init__(self, client, "incident_reports", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, IncidentReports)
        IPaginateable.__init__(self, IncidentReports)

    def id(self, id: int) -> IncidentreportsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized IncidentreportsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            IncidentreportsIdEndpoint: The initialized IncidentreportsIdEndpoint object.
        """
        child = IncidentreportsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: SimpleSatRequestParams | None = None,
    ) -> PaginatedResponse[IncidentReports]:
        """
        Performs a GET request against the /incident_reports endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[IncidentReports]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["limit"] = limit
        else:
            params = {"page": page, "limit": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            IncidentReports,
            self,
            "incident_reports",
            page,
            limit,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: SimpleSatRequestParams | None = None,
    ) -> IncidentReports:
        """
        Performs a GET request against the /incident_reports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AuthInformation: The parsed response data.
        """
        return self._parse_many(
            IncidentReports,
            super()._make_request("GET", data=data, params=params).json().get('incident_reports', {}),
        )
