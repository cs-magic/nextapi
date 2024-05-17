'''
ref: https://www.volcengine.com/docs/82379/1263279
'''

from __future__ import print_function
import volcenginesdkcore
import volcenginesdkark
from pprint import pprint
from volcenginesdkcore.rest import ApiException

from settings import settings

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = settings.DOUBAO_AK
    configuration.sk = settings.DOUBAO_SK
    configuration.region = "cn-beijing"
    # set default configuration
    volcenginesdkcore.Configuration.set_default(configuration)
    
    # use global default configuration
    api_instance = volcenginesdkark.ARKApi()
    get_api_key_request = volcenginesdkark.GetApiKeyRequest(
        duration_seconds=30 * 24 * 3600,
        resource_type="endpoint",
        resource_ids=[
            # todo: what's the endpoint_id ?
            "${YOUR_ENDPOINT_ID}"
        ],
    )
    
    try:
        resp = api_instance.get_api_key(get_api_key_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
