from pysimplesat.endpoints.base.base_endpoint import SimpleSatEndpoint
from pysimplesat.endpoints.simplesat.SignalsIdEndpoint import SignalsIdEndpoint
from pysimplesat.interfaces import (
    IGettable,
    IPaginateable,
)
from pysimplesat.models.simplesat import Signals
from pysimplesat.responses.paginated_response import PaginatedResponse
from pysimplesat.types import (
    JSON,
    SimpleSatRequestParams,
)


class SignalsEndpoint(
    SimpleSatEndpoint,
    IGettable[Signals, SimpleSatRequestParams],
    IPaginateable[Signals, SimpleSatRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        SimpleSatEndpoint.__init__(self, client, "signals", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Signals)
        IPaginateable.__init__(self, Signals)

    def id(self, id: int) -> SignalsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SignalsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SignalsIdEndpoint: The initialized SignalsIdEndpoint object.
        """
        child = SignalsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: SimpleSatRequestParams | None = None,
    ) -> PaginatedResponse[Signals]:
        """
        Performs a GET request against the /signals endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Signals]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["limit"] = limit
        else:
            params = {"page": page, "limit": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Signals,
            self,
            "signals",
            page,
            limit,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: SimpleSatRequestParams | None = None,
    ) -> Signals:
        """
        Performs a GET request against the /signals endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AuthInformation: The parsed response data.
        """
        return self._parse_many(
            Signals,
            super()._make_request("GET", data=data, params=params).json().get('signals', {}),
        )
