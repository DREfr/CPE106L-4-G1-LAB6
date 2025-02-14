from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Get the 'chinook' database
db = client["chinook"]

# Get the 'albums' collection
albums_collection = db["albums"]

# Find all albums and print the artist name with the album title
for album in albums_collection.find():
    artist = db.artists.find_one({"ArtistId": album["ArtistId"]})
    print(f"Artist: {artist['Name']}, Album: {album['Title']}")
    
client.close()


    