import boto3
import pymysql
import json

client = boto3.client(
    service_name="secretsmanager",
    region_name="us-east-1"
)

response = client.get_secret_value(
    SecretId="arn:aws:secretsmanager:us-east-1:692859923876:secret:rds!db-4d61454d-c0f3-4eee-80e1-129c84742eb1-ELKBp7"
)

secret = json.loads(response["SecretString"])

username = secret["username"]
password = secret["password"]
host = "library-dashboard.cwb6w8gi2rzj.us-east-1.rds.amazonaws.com"
port = 3306
dbname = "library-dashboard"

connection = pymysql.connect(
    host=host,
    port=port,
    user=username,
    password=password,
    database=dbname
)

cursor = connection.cursor()