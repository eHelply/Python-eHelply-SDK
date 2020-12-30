from typing import Union, Type, TypeVar

import requests

from ehelply_python_sdk.utils import SDKConfiguration, make_requests
from ehelply_python_sdk.services import services
from ehelply_python_sdk.services.service_schemas import is_response_error, ErrorResponse

genericSDKBase = TypeVar('genericSDKBase', bound=services.SDKBase)


class eHelplySDK:
    """
    eHelply SDK
    """
    def __init__(self, sdk_configuration: SDKConfiguration) -> None:
        self.sdk_configuration: SDKConfiguration = sdk_configuration
        self.requests_session: requests.Session = make_requests(sdk_configuration=sdk_configuration)

    def _make_client(
            self,
            client: str,
            sdk_configuration: SDKConfiguration = None,
            request_session: requests.Session = None
    ) -> genericSDKBase:
        if not sdk_configuration:
            sdk_configuration = self.sdk_configuration

        if not request_session:
            request_session = self.requests_session

        if client == "access":
            return services.AccessSDK(sdk_configuration=sdk_configuration, requests_session=request_session)

        if client == "security":
            return services.SecuritySDK(sdk_configuration=sdk_configuration, requests_session=request_session)

    def make_access(
            self,
            sdk_configuration: SDKConfiguration = None,
            request_session: requests.Session = None
    ) -> services.AccessSDK:
        return self._make_client(
            client="access",
            sdk_configuration=sdk_configuration,
            request_session=request_session
        )

    def make_security(
            self,
            sdk_configuration: SDKConfiguration = None,
            request_session: requests.Session = None
    ) -> services.AccessSDK:
        return self._make_client(
            client="security",
            sdk_configuration=sdk_configuration,
            request_session=request_session
        )