from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Get the 'chinook' database
db = client["chinook"]

# Get the 'tracks' collection
tracks_collection = db["tracks"]

# Find all tracks from a specific album (e.g., album with AlbumId 1)
album_tracks = tracks_collection.find({"AlbumId": 1})

print(f"==========Album 1==========")
for track in album_tracks:
    print(f"Track Name: {track['Name']}")

# Find all tracks from a specific album (e.g., album with AlbumId 20)
album_tracks = tracks_collection.find({"AlbumId": 20})

print(f"==========Album 20==========")
for track in album_tracks:
    print(f"Track Name: {track['Name']}")

    
client.close()