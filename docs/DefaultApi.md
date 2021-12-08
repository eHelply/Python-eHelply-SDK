# ehelply-python-sdk.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playground_notes_playground_get**](DefaultApi.md#playground_notes_playground_get) | **GET** /notes/notes/playground | Playground


# **playground_notes_playground_get**
> bool, date, datetime, dict, float, int, list, str, none_type playground_notes_playground_get()

Playground

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Playground
        api_response = api_instance.playground_notes_playground_get()
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling DefaultApi->playground_notes_playground_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

