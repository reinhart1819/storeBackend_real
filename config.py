import pymongo
import certifi



con_str = "mongodb+srv://reinhart1819:school3818919@cluster0.giaho.mongodb.net/?retryWrites=true&w=majority"


client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("BBEGStore")
