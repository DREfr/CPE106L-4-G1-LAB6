from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Get the 'chinook' database
db = client["chinook"]

# Get the 'artists' collection
artists_collection = db["artists"]

# Print all artists
for artist in artists_collection.find():
    print(artist['Name'])
    
client.close()