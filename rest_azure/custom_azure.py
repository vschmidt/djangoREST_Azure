from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'djangorestazure' # Must be replaced by your <storage_account_name>
    account_key = 'MzkavMWEiMFsRq7roIgbR1j55zVAzuun/9pNP8DUpPc8os3pNqMQG3MWYAZqOwUc+aQaUELObs39xxfmVxj+zg==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'djangorestazure' # Must be replaced by your storage_account_name
    account_key = 'MzkavMWEiMFsRq7roIgbR1j55zVAzuun/9pNP8DUpPc8os3pNqMQG3MWYAZqOwUc+aQaUELObs39xxfmVxj+zg==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None