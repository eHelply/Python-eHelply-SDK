from ehelply_python_sdk.sdk import SDKConfiguration, eHelplySDK, ErrorResponse, is_response_error

CONST_ACCESS_TOKEN: str = "7UlOkrKuU8rOBESH75337748495211ebbae002d5643456f6jV7UlOkrKuU8rOBE"
CONST_SECRET_TOKEN: str = "EjNclyR8DMyM45r374c07f974ae24bdabcdb3228e8929a467m8VwxuhaBAb_KFj"


def make_sdk(project: str = "ehelply-resources") -> eHelplySDK:
    return eHelplySDK(
        sdk_configuration=SDKConfiguration(
            access_token=CONST_ACCESS_TOKEN,
            secret_token=CONST_SECRET_TOKEN,
            project_identifier=project,
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


def test_create_key_and_attach():
    sdk: eHelplySDK = make_sdk(project="ehelply-cloud")

    from ehelply_python_sdk.services.security.sdk import SecuritySDK, CreateKey, CreateKeyResponse
    from ehelply_python_sdk.utils import make_requests

    # Have to do it this way to test access locally, but use test env security service
    sdk_config = SDKConfiguration(
        access_token=CONST_ACCESS_TOKEN,
        secret_token=CONST_SECRET_TOKEN,
        project_identifier="ehelply-cloud",
        base_url_override="https://api.test.ehelply.com"
    )

    security_only_sdk = SecuritySDK(
        sdk_configuration=sdk_config,
        requests_session=make_requests(sdk_configuration=sdk_config)
    )

    access_client = sdk.make_access()

    key: CreateKeyResponse = security_only_sdk.create_key(key=CreateKey(name="Test key", summary="Test key"))

    response = access_client.attach_key_to_entity(
        entity_identifier="da1b58a4-4963-11eb-a0ca-022586ccdf28",
        key_uuid=key.uuid
    )

    print(key.dict())
    print(response.dict())

    # response = access_client.search_types(name="eHelply Access")
    #
    # if is_response_error(response):
    #     response: ErrorResponse = response
    #     print("I'm sadness")
    #     print(response.status_code)
    #     print(response.message)
    # else:
    #     print(response.dict())


def test_complex_authrules():
    from ehelply_python_sdk.services.access.sdk import AccessSDK, AuthModel
    from ehelply_python_sdk.services.access.auth_rules import AuthRule
    from ehelply_python_sdk.utils import make_requests

    sdk_config = SDKConfiguration(
        access_token="XUxGcshq23146db04af511eb8b1202d5643456f664v2kXoZ",
        secret_token="J5SVI8-N7c199c43675242a48b6b1a05808c6770CqOP2Vu0",
        project_identifier="my_project_uuid",
        base_url_override="http://localhost"
    )

    access_only_sdk = AccessSDK(
        sdk_configuration=sdk_config,
        requests_session=make_requests(sdk_configuration=sdk_config)
    )

    auth_model: AuthModel = AuthModel(
        access_sdk=access_only_sdk,
        active_participant_uuid="da1b58a4-4963-11eb-a0ca-022586ccdf28",
        entity_identifier="fs-user-bob-magob"
    )

    response = access_only_sdk.is_allowed(
        auth_model=auth_model,
        # target_identifier="fs-schedule-random_uuid_goes_here",
        # node="fs.schedules.view",
        node='ehelply.access.types.get',
        target_identifier='ehelply-access.service'
    )

    print(response)

    AuthRule(
        auth_model,
        AuthRule(auth_model).participant_has_node_on_target(
            partition='ehelply-resources',
            node='fs.schedules.view',
            target_identifier='fs-schedule-random_uuid_goes_here'
        ),
        AuthRule(auth_model).participant_has_node_on_target(
            partition='my_project_uuid',
            node='ehelply.access.types.get',
            target_identifier='ehelply-access.service'
        )
    ).verify()

    # if is_response_error(response):
    #     response: ErrorResponse = response
    #     print("I'm sadness")
    #     print(response.status_code)
    #     print(response.message)
    # else:
    #     print(response.dict())
