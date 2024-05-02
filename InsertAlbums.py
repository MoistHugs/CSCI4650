import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# Define the table name
table_name = 'Albums'

# Define the items to be inserted
items = [
    {
        'Artist': {'S': 'Piano Man'},
        'Songs': {'S': 'Billy Joel'},
        'Album': {'S': 'Piano Man'},
        'ReleaseYear': {'N': '1973'}  # Example extra attribute
    },
    {
        'Artist': {'S': 'Eminem'},
        'Songs': {'S': 'Lose Yourself'},
        'Album': {'S': '8 Mile Soundtrack'},
        'ReleaseYear': {'N': '2002'}  # Example extra attribute
    },
    {
        'Artist': {'S': 'Queen'},
        'Songs': {'S': 'Bohemian Rhapsody'},
        'Album': {'S': 'A Night at the Opera'},
        'ReleaseYear': {'N': '1975'}  # Example extra attribute
    }
]

# Insert items into the table
for item in items:
    response = dynamodb.put_item(
        TableName=table_name,
        Item=item
    )
    print("Item inserted successfully:", item)
