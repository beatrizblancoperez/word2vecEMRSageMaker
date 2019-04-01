import boto3
import json

endpoint_name = 'word2vecendpoint'
runtime = boto3.Session().client(service_name='sagemaker-runtime',region_name='eu-west-1')

input_json = json.dumps({"input":"science"})


response = runtime.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/json', Body=input_json)
print(response['Body'].read())