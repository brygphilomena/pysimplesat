import typing
from datetime import datetime, timezone
import base64

from pysimplesat.clients.base_client import SimpleSatClient
from pysimplesat.config import Config

if typing.TYPE_CHECKING:
    from pysimplesat.endpoints.simplesat.AccountEndpoint import AccountEndpoint
    from pysimplesat.endpoints.simplesat.ActorEndpoint import ActorEndpoint
    from pysimplesat.endpoints.simplesat.AgentsEndpoint import AgentsEndpoint
    from pysimplesat.endpoints.simplesat.BillingreportsEndpoint import BillingreportsEndpoint
    from pysimplesat.endpoints.simplesat.IncidentreportsEndpoint import IncidentreportsEndpoint
    from pysimplesat.endpoints.simplesat.OrganizationsEndpoint import OrganizationsEndpoint
    from pysimplesat.endpoints.simplesat.ReportsEndpoint import ReportsEndpoint
    from pysimplesat.endpoints.simplesat.SignalsEndpoint import SignalsEndpoint


class SimpleSatAPIClient(SimpleSatClient):
    """
    SimpleSat API client. Handles the connection to the SimpleSat API
    and the configuration of all the available endpoints.
    """

    def __init__(
        self,
        privatekey: str,
    ) -> None:
        """
        Initializes the client with the given credentials.

        Parameters:
            privatekey (str): Your SimpleSat API private key.
        """
        self.privatekey: str = privatekey
        self.token_expiry_time: datetime = datetime.now(tz=timezone.utc)

    # Initializing endpoints
    @property
    def account(self) -> "AccountEndpoint":
        from pysimplesat.endpoints.simplesat.AccountEndpoint import AccountEndpoint

        return AccountEndpoint(self)

    @property
    def actor(self) -> "ActorEndpoint":
        from pysimplesat.endpoints.simplesat.ActorEndpoint import ActorEndpoint

        return ActorEndpoint(self)

    @property
    def agents(self) -> "AgentsEndpoint":
        from pysimplesat.endpoints.simplesat.AgentsEndpoint import AgentsEndpoint

        return AgentsEndpoint(self)

    @property
    def billing_reports(self) -> "BillingreportsEndpoint":
        from pysimplesat.endpoints.simplesat.BillingreportsEndpoint import BillingreportsEndpoint

        return BillingreportsEndpoint(self)

    @property
    def incident_reports(self) -> "IncidentreportsEndpoint":
        from pysimplesat.endpoints.simplesat.IncidentreportsEndpoint import IncidentreportsEndpoint

        return IncidentreportsEndpoint(self)

    @property
    def organizations(self) -> "OrganizationsEndpoint":
        from pysimplesat.endpoints.simplesat.OrganizationsEndpoint import OrganizationsEndpoint

        return OrganizationsEndpoint(self)

    @property
    def reports(self) -> "ReportsEndpoint":
        from pysimplesat.endpoints.simplesat.ReportsEndpoint import ReportsEndpoint

        return ReportsEndpoint(self)

    @property
    def signals(self) -> "SignalsEndpoint":
        from pysimplesat.endpoints.simplesat.SignalsEndpoint import SignalsEndpoint

        return SignalsEndpoint(self)

    def _get_url(self) -> str:
        """
        Generates and returns the URL for the SimpleSat API endpoints based on the company url and codebase.
        Logs in an obtains an access token.
        Returns:
            str: API URL.
        """
        return f"https://api.simplesat.io/api/v1"

    def _get_headers(self) -> dict[str, str]:
        """
        Generates and returns the headers required for making API requests. The access token is refreshed if necessary before returning.

        Returns:
            dict[str, str]: Dictionary of headers including Content-Type, Client ID, and Authorization.
        """
        return {
            "Content-Type": "application/json",
            "X-Simplesat-Token": f"{self.privatekey}",
        }
