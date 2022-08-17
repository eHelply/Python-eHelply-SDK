# GetInvoiceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_uuid** | **str** |  | 
**line_items** | [**[LineItem]**](LineItem.md) |  | 
**subtotal** | **int** |  | 
**discounts** | [**[Discount]**](Discount.md) |  | 
**taxes** | [**[Tax]**](Tax.md) |  | 
**total** | **int** |  | 
**notes** | [**[Note]**](Note.md) |  | 
**created_at** | **str** |  | 
**update_at** | **str** |  | 
**paid** | **bool** |  | [optional]  if omitted the server will use the default value of False
**deleted_at** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


