from pymongo import MongoClient

client = MongoClient("localhost:27017")
#the above line creates a connection with the MongoDB database

db = client.employee_application # name of our database

# Now we need to make collections (same as tables in relational databases)
collection_name = db["employees_app"]
