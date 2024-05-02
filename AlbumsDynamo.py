import boto3
import time

# Initialize the DynamoDB client with the specified region
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

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
try:
    response = dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definitions,
        ProvisionedThroughput=provisioned_throughput
    )

    # Wait until the table is created
    while True:
        response = dynamodb.describe_table(TableName=table_name)
        table_status = response['Table']['TableStatus']
        print("Table status:", table_status)
        
        if table_status == 'ACTIVE':
            print("Table 'Albums' created successfully!")
            break
        elif table_status == 'CREATING':
            time.sleep(5)  # Wait for 5 seconds before checking again
        else:
            print("Table creation failed. Status:", table_status)
            break

except dynamodb.exceptions.ResourceInUseException:
    print(f"Table '{table_name}' already exists. Skipping creation.")
except Exception as e:
    print("An error occurred:", str(e))
