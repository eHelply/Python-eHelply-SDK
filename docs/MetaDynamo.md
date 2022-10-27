# MetaDynamo

A meta from DynamoDB

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**basic** | [**Basic**](Basic.md) |  | [optional] 
**detailed** | [**Detailed**](Detailed.md) |  | [optional] 
**custom** | [**MetaCustom**](MetaCustom.md) |  | [optional] 
**dates** | [**DatesMeta**](DatesMeta.md) |  | [optional] 
**fields** | [**[Field]**](Field.md) |  | [optional] 
**children** | [**[MetaChildren]**](MetaChildren.md) |  | [optional]  if omitted the server will use the default value of []
**parent_uuid** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


