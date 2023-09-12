import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="de-youtube-cleaned-data-statistics",
    table_name="cleansed_raw_statisticscleansed_raw_statistics",
    transformation_ctx="AWSGlueDataCatalog_node1",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog = glueContext.create_dynamic_frame.from_catalog(
    database="de-youtube-cleaned-data-statistics",
    table_name="cleaned_statistics_reference_data",
    transformation_ctx="AWSGlueDataCatalog",
)

# Script generated for node Join
Join_node = Join.apply(
    frame1=AWSGlueDataCatalog,
    frame2=AWSGlueDataCatalog_node1,
    keys1=["id"],
    keys2=["category_id"],
    transformation_ctx="Join_node",
)

# Script generated for node Amazon S3
AmazonS3_node = glueContext.getSink(
    path="s3://de-youtube-data-analysis/final_analysis/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["region", "category_id"],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node",
)
AmazonS3_node.setCatalogInfo(
    catalogDatabase="db_youtube_analysis", catalogTableName="final_analysis"
)
AmazonS3_node.setFormat("glueparquet")
AmazonS3_node.writeFrame(Join_node)
job.commit()
