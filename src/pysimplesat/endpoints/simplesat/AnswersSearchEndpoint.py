from pysimplesat.endpoints.base.base_endpoint import SimpleSatEndpoint
from pysimplesat.interfaces import (
    IPostable,
)
from pysimplesat.models.simplesat import Answer
from pysimplesat.types import (
    JSON,
    SimpleSatRequestParams,
)


class AnswersSearchEndpoint(
    SimpleSatEndpoint,
    IPostable[Answer, SimpleSatRequestParams],

):
    def __init__(self, client, parent_endpoint=None) -> None:
        SimpleSatEndpoint.__init__(self, client, "search", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, Answer)

    #TODO: How do I paginate a post?
    def post(self, data: JSON | None = None, params: SimpleSatRequestParams | None = None) -> Answer:
        """
        Performs a POST request against the /answers/search endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Survey: The parsed response data.
        """
        return self._parse_many(Answer, super()._make_request("POST", data=data, params=params).json().get('answers', {}))
