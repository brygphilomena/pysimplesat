from pysimplesat.endpoints.base.base_endpoint import BaseEndpoint
from pysimplesat.interfaces import (
    IGettable,
)
from pysimplesat.models.simplesat import Account
from pysimplesat.types import (
    JSON,
    SimpleSatRequestParams,
)


class AccountEndpoint(
    SimpleSatEndpoint,
    IGettable[Account, SimpleSatRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        SimpleSatEndpoint.__init__(self, client, "account", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Account)

    def get(
        self,
        data: JSON | None = None,
        params: SimpleSatRequestParams | None = None,
    ) -> Account:
        """
        Performs a GET request against the /account endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AuthInformation: The parsed response data.
        """
        return self._parse_one(
            Account,
            super()._make_request("GET", data=data, params=params).json().get('account', {}),
        )
