from ehelply_python_sdk.sdk import SDKConfiguration, eHelplySDK, is_response_error


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

    print(response.status_code)

    print(response.dict())
