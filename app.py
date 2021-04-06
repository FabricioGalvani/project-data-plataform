from athena.stack import AthenaStack
from aws_cdk import core

from data_platform.data_lake.stack import DataLakeStack
from glue_catalog.stack import GlueCatalogStack


app = core.App()

data_lake = DataLakeStack(app)
glue_catalog = GlueCatalogStack(app, data_lake_bucket=data_lake_raw_bucket)
athena_stack = AthenaStack(app)
kinesis_stack = KinesisStack(app, data_lake_raw_bucket=data_lake.data_lake_raw_bucket)

.synth()












