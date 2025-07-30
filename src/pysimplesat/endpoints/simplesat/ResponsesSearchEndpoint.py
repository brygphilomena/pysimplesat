from pysimplesat.endpoints.base.base_endpoint import SimpleSatEndpoint
from pysimplesat.interfaces import (
    IPostable,
)
from pysimplesat.models.simplesat import Response
from pysimplesat.types import (
    JSON,
    SimpleSatRequestParams,
)


class ResponsesSearchEndpoint(
    SimpleSatEndpoint,
    IPostable[Response, SimpleSatRequestParams],

):
    def __init__(self, client, parent_endpoint=None) -> None:
        SimpleSatEndpoint.__init__(self, client, "search", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, Response)

    #TODO: How do I paginate a post?
    def post(self, data: JSON | None = None, params: SimpleSatRequestParams | None = None) -> Response:
        """
        Performs a POST request against the /responses/search endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Survey: The parsed response data.
        """
        return self._parse_many(Response, super()._make_request("POST", data=data, params=params).json().get('responses', {}))
