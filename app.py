from athena.stack import AthenaStack
from aws_cdk import core

from data_platform.data_lake.stack import DataLakeStack
from dms.stack import DmsStack
from glue_catalog.stack import GlueCatalogStack
from kinesis.stack import KinesisStack

from common_stack import CommonStack

app = core.App()

data_lake = DataLakeStack(app)
glue_catalog = GlueCatalogStack(app, data_lake_bucket=data_lake.data_lake_raw_bucket)
athena_stack = AthenaStack(app)
kinesis_stack = KinesisStack(app, data_lake_raw_bucket=data_lake.data_lake_raw_bucket)
common_stack = CommonStack(app)
dms_stack = DmsStack(
    app, data_lake_raw_bucket=data_lake.data_lake_raw_bucket, common_stack=common_stack
)

app.synth()
