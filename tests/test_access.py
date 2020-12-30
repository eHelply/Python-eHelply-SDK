from ehelply_python_sdk.sdk import SDKConfiguration, eHelplySDK, ErrorResponse, is_response_error


CONST_ACCESS_TOKEN: str = "7UlOkrKuU8rOBESH75337748495211ebbae002d5643456f6jV7UlOkrKuU8rOBE"
CONST_SECRET_TOKEN: str = "EjNclyR8DMyM45r374c07f974ae24bdabcdb3228e8929a467m8VwxuhaBAb_KFj"


def make_sdk() -> eHelplySDK:
    return eHelplySDK(
        sdk_configuration=SDKConfiguration(
            access_token=CONST_ACCESS_TOKEN,
            secret_token=CONST_SECRET_TOKEN,
            project_identifier="ehelply-resources",
            base_url_override="http://localhost"
        )
    )


def test_search_types():
    sdk: eHelplySDK = make_sdk()

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
        access_token=CONST_ACCESS_TOKEN,
        secret_token=CONST_SECRET_TOKEN,
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


def test_authrules_entity_has_node_on_target():
    from ehelply_python_sdk.services.access.auth_rules import AuthRule, AuthModel

    sdk: eHelplySDK = make_sdk()

    access_client = sdk.make_access()

    auth_model: AuthModel = AuthModel(
        access_sdk=access_client,
        # access_token=CONST_ACCESS_TOKEN,
        # secret_token=CONST_SECRET_TOKEN,
        entity_identifier="ehelply-access-root-admin"
    )

    AuthRule(
        auth_model,
        AuthRule(auth_model).entity_has_node_on_target(
            node="ehelply.access.types.get",
            target_identifier="ehelply-access.service"
        )
    ).verify()
