from aws_cdk import core

from data_platform.data_lake.stack import DataLakeStack


app = core.App()
data_lake = DataLakeStack(app)
app.synth()
