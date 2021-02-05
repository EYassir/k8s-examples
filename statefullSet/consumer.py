import boto3
import json
from datetime import datetime
import time

my_stream_name = 'weather-stream'

kinesis_client = boto3.client('kinesis', region_name='us-east-1')

response = kinesis_client.describe_stream(StreamName=my_stream_name)

my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']
shard_iterator = kinesis_client.get_shard_iterator(StreamName=my_stream_name,
                                                      ShardId=my_shard_id,
                                                      ShardIteratorType='LATEST')
my_shard_iterator = shard_iterator['ShardIterator']
record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator,

cluster = Cluster(['54.170.208.118:31308'])
session = cluster.connect()
c_sql = """CREATE TABLE IF NOT EXISTS employee (emp_id int PRIMARY KEY, ename varchar, sal double, city varchar);"""
session.execute(c_sql)
while 'NextShardIterator' in record_response:
    record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'], Limit=2)
    print (record_response)
    insert_sql = session.prepare("INSERT INTO  employee (emp_id, ename , sal,city) VALUES (?,?,?,?)")
    batch = BatchStatement()
    batch.add(insert_sql, (record_response[1], record_response[2], record_response[3], record_response[4]))
    # wait for 5 seconds
    time.sleep(5)


rows = session.execute('select * from employee limit 5;')
for row in rows:
    print(row.ename, row.sal)