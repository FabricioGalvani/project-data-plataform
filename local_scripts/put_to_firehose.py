import configparser
import os
import boto3
import json
from fake_web_events import Simulation


def _get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


config = configparser.ConfigParser()
path = _get_abs_path("configkeys.dev")
config.read(path)

aws_access_key_id = config["aws"]["aws_access_key_id"]
aws_secret_access_key = config["aws"]["aws_secret_access_key"]
region_name = config["aws"]["region_name"]

client = boto3.client(
    "firehose",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name,
)


def put_record(event):
    data = json.dumps(event) + "\n"

    response = client.put_record(
        DeliveryStreamName="firehose-dev-raw-delivery-stream",
        Record={"Data": data},
    )
    print(event)
    return response


simulation = Simulation(user_pool_size=100, sessions_per_day=1000)
events = simulation.run(duration_seconds=10000)

for event in events:
    put_record(event)
