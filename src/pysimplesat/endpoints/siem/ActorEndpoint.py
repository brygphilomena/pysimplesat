from pysimplesat.endpoints.base.base_endpoint import SimpleSatEndpoint
from pysimplesat.interfaces import (
    IGettable,
)
from pysimplesat.models.simplesat import ActorResponse
from pysimplesat.types import (
    JSON,
    SimpleSatRequestParams,
)


class ActorEndpoint(
    SimpleSatEndpoint,
    IGettable[ActorResponse, SimpleSatRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        SimpleSatEndpoint.__init__(self, client, "actor", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, ActorResponse)

    def get(
        self,
        data: JSON | None = None,
        params: SimpleSatRequestParams | None = None,
    ) -> ActorResponse:
        """
        Performs a GET request against the /Actor endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AuthInformation: The parsed response data.
        """
        return self._parse_one(
            ActorResponse,
            super()._make_request("GET", data=data, params=params).json(),
        )
