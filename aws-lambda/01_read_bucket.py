import boto3
import json

bucket_name = 'aws-cloudtrail-logs-248367286364-78494363'
cloud_trail_log = '02_s3_test_data.json'
keypair_name = 'PlatformxRND'


def load_data(log_json):
    with open(log_json) as data:
        data_dump = json.load(data)
    return data_dump


def list_buckets():
    s3 = boto3.resource("s3")
    for bucket in s3.buckets.all():
        print(bucket.name)


def print_bucket_object_keys(bucket):
    s3 = boto3.resource("s3")
    for obj in s3.Bucket(bucket).objects.all():
        print(obj.key)


def lambda_handler(event, context):
    print(f"Start reading latest object from {bucket_name}")
    s3 = boto3.resource('s3')
    try:
        for rec in event['Records']:
            if rec['eventName'] == 'DeleteKeyPair' and rec['requestParameters']['keyName'] == keypair_name:
                raise RuntimeError("KeyPair Deleted")
            else:
                print(f"KeyPair {keypair_name} exists")
    except Exception as e:
        print(e)
        print(f"Keypair {keypair_name} deleted or error with validating keypair {keypair_name} deletion in bucket logs: {bucket_name}")


records = load_data(cloud_trail_log)
lambda_handler(records, '')