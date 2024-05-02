import boto3

# Initialize the DynamoDB client with the specified region
dynamodb = boto3.client('dynamodb', region_name='us-east-1')  # Change 'us-east-1' to your desired region

# Define the table schema
table_name = 'Albums'
key_schema = [
    {
        'AttributeName': 'Album',
        'KeyType': 'HASH'  # Partition key
    },
    {
        'AttributeName': 'Songs',
        'KeyType': 'RANGE'  # Sort key
    }
]
attribute_definitions = [
    {
        'AttributeName': 'Album',
        'AttributeType': 'S'  # String type for partition key
    },
    {
        'AttributeName': 'Songs',
        'AttributeType': 'S'  # String type for sort key
    }
]

# Define provisioned throughput
provisioned_throughput = {
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}

# Create the DynamoDB table
response = dynamodb.create_table(
    TableName=table_name,
    KeySchema=key_schema,
    AttributeDefinitions=attribute_definitions,
    ProvisionedThroughput=provisioned_throughput
)

# Wait until the table is created
table_description = None
while table_description is None or table_description['TableStatus'] != 'ACTIVE':
    table_description = dynamodb.describe_table(TableName=table_name)
    print("Table status:", table_description['TableStatus'])

print("Table 'Albums' created successfully!")
