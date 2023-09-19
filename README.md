# Youtube-Data-Analysis
## Overview
This project aims to securely manage, streamline, and perform analysis on the structured and semi-structured YouTube videos data based on the video categories and the trending metrics.
## Dataset
The dataset has been taken from kaggle. This dataset includes several months (and counting) of data on daily trending YouTube videos. Data is included for the US, GB, DE, CA, and FR regions (USA, Great Britain, Germany, Canada, and France, respectively), with up to 200 listed trending videos per day.

Link of dataset: https://www.kaggle.com/datasets/datasnaek/youtube-new

## Architecture
![architecture](https://github.com/thiruveedhulaMANAS/youtube-data-analysis/assets/88129091/91207136-aa44-4d42-862e-9504a0d20c81)

## AWS Services used

1. **AWS S3**: Amazon Simple Storage Service (S3) is a scalable object storage service designed to store and retrieve data, making it extremely dependable and accessible through the internet.

2. **AWS Lambda**: AWS Lambda is a serverless computing service that allows you to run code in response to events while automatically managing the infrastructure necessary to execute your code.

3. **AWS Glue**: AWS Glue is a fully managed extract, transform, and load (ETL) service that simplifies data integration by making it simple to transport and convert data across multiple data stores.

4. **Amazon Athena**: Amazon Athena is a serverless query service that allows you to analyse data in Amazon S3 using conventional SQL, removing the need for complicated ETL operations.

5. **Amazon QuickSight**: Amazon QuickSight is a cloud-based business intelligence solution that allows customers to create interactive data visualisations and dashboards for enhanced data-driven decision-making.

6. **IAM (Identity and Access Management)**: IAM is an AWS service that lets you securely restrict access to your resources by managing users, groups, roles, and permissions, ensuring only authorised users may interact with AWS services and resources.

## Process

**Step 1:** Begin by creating an IAM role to control access rights for the services we'll be utilising during this process, such as S3, Lambda, Glue, Athena, and QuickSight.

**Step 2:** Place your data in an Amazon S3 bucket.

**Step 3:** Make a Lambda function that converts the data from JSON to Parquet. This converter will optimize data for Athena querying efficiency.

**Step 4:** Place the cleaned Parquet format files back into the S3 bucket, making them available for further processing.

**Step 5:** Use AWS Glue to create an ETL job to convert and prepare the data for analysis. This task will assist you in producing a final dataset that is ready for analysis.

**Step 6:** After correctly preparing your data, utilize Amazon Athena to execute SQL-based analysis on the dataset stored in your S3 bucket. Athena enables you to query your data without requiring complicated ETL operations.

**Step 7:** Finally, use Amazon QuickSight to see and analyze your data. QuickSight will assist you in creating interactive data visualizations and dashboards from your analyzed dataset.

## Output ##
![output-1](https://github.com/thiruveedhulaMANAS/youtube-data-analysis/blob/main/outputs/Screenshot%20(1).png)
![output-2](https://github.com/thiruveedhulaMANAS/youtube-data-analysis/blob/main/outputs/Screenshot%20(2).png)
![output-3](https://github.com/thiruveedhulaMANAS/youtube-data-analysis/blob/main/outputs/Screenshot%20(3).png)
