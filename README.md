# airflow-etl-project

In the project, i created an end-to-end data engineering project using airflow, python, pandas, AWS EC2 and S3

# Packages to install are:

- Pandas
- tweepy : I used this package to access the twitter data
- s3fs : used to read, store and write data on s3 bucket.

* airflow

# Note

- for you to access the "Twitter API v2" you need to upgrade from Essential to Elevated for free.

* create an IAM role with s3fullaccess and ec2fullaccess and attach it to your EC2 instance thereby giving airflow permission to tranfer the csv file to your s3 bucket folder.
