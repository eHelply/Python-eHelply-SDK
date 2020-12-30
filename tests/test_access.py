from ehelply_python_sdk.sdk import SDKConfiguration, eHelplySDK, ErrorResponse, is_response_error


def test_search_types():
    sdk: eHelplySDK = eHelplySDK(
        sdk_configuration=SDKConfiguration(
            access_token="",
            secret_token="",
            project_identifier="ehelply-resources",
            base_url_override="http://localhost"
        )
    )

    access_client = sdk.make_access()

    response = access_client.search_types(name="eHelply Access")

    if is_response_error(response):
        response: ErrorResponse = response
        print("I'm sadness")
        print(response.status_code)
        print(response.message)
    else:
        print(response.dict())


def test_access_only_sdk():
    from ehelply_python_sdk.services.access.sdk import AccessSDK
    from ehelply_python_sdk.utils import make_requests

    sdk_config = SDKConfiguration(
        access_token="",
        secret_token="",
        project_identifier="ehelply-resources",
        base_url_override="http://localhost"
    )

    access_only_sdk = AccessSDK(
        sdk_configuration=sdk_config,
        requests_session=make_requests(sdk_configuration=sdk_config)
    )

    response = access_only_sdk.search_types(name="eHelply Access")

    if is_response_error(response):
        response: ErrorResponse = response
        print("I'm sadness")
        print(response.status_code)
        print(response.message)
    else:
        print(response.dict())

