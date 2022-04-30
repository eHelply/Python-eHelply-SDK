# PlaceResponse

**:param** name                                **type:** string **:param** summary                             **type:** string or None  **:param** public                              **type:** bool or None  **:param** meta                                **type:** dict or None  **:param** addresses                           **type:** PlaceAddress or None  **:param** contact                             **type:** ContactBase or None

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**summary** | **str** |  | [optional] 
**public** | **bool** |  | [optional]  if omitted the server will use the default value of True
**meta** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**addresses** | **[AddressBase]** |  | [optional] 
**contact** | [**ContactBase**](ContactBase.md) |  | [optional] 
**uuid** | **str** |  | 
**project_uuid** | **str** |  | [optional] 
**meta_uuid** | **str** |  | [optional] 
**catalog_data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional]  if omitted the server will use the default value of {}
**review_group_data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional]  if omitted the server will use the default value of {}
**schedule_data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional]  if omitted the server will use the default value of {}
**collection_data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional]  if omitted the server will use the default value of {}
**blog_data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional]  if omitted the server will use the default value of {}
**tags** | **[TagBase]** |  | [optional] 
**categories** | **[CategoryBase]** |  | [optional] 
**company** | **object** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**deleted_at** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

