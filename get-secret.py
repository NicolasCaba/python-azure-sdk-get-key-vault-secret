import logging
import os
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import AzureError
from azure.identity import ClientSecretCredential

keyVaultName = 'key-vault-outputs'
secretName = 'vnet-name'


def getKeyVaultSecret(keyVaultName, secretName):
    try:
        KVUri = f"https://{keyVaultName}.vault.azure.net"

        client_id = os.environ['AZURE_CLIENT_ID']
        client_secret = os.environ['AZURE_CLIENT_SECRET']
        tenant_id = os.environ['AZURE_TENANT_ID']

        credentials = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
        client = SecretClient(vault_url=KVUri, credential=credentials)

        retrieved_secret = client.get_secret(secretName)

        print(f"{secretName} = {retrieved_secret.value}")
    
    except AzureError as error:
        logging.error(error)



getKeyVaultSecret(keyVaultName, secretName)



