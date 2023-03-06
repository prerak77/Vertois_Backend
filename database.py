import os
import json

from azure.cosmos import CosmosClient, PartitionKey



ENDPOINT = 'https://de44a99c-0ee0-4-231-b9ee.documents.azure.com:443/'
KEY = 'dJL5ctFaJWB3YUzdl9sUQt5N1VziPj7G9KDf0z6s5zwpyYoDdvAx0GpSESCHCE5IwF072ML7FdpmACDb1hiQBA=='


DATABASE_NAME = "Vertois"
CONTAINER_NAME = "Container1"

client = CosmosClient(url=ENDPOINT, credential=KEY)

def CREATE_DATABASE():
    global database,key_path,container
    database= client.create_database_if_not_exists(id=DATABASE_NAME)

    key_path = PartitionKey(path="/Vertois")

    container = database.create_container_if_not_exists(
        id=CONTAINER_NAME, partition_key=key_path, offer_throughput=400
    )

def ADDING_NEW_ELEMENT(data):

    KEYS = list(data["content"].keys())
    VALUES = list(data["content"].values())

    new_item = {
         "id":     VALUES[0],
         "Vertois":"section1",
         KEYS[1]: VALUES[1],
         KEYS[2]: VALUES[2],
         KEYS[3]: VALUES[3],
         KEYS[4]: VALUES[4],
         KEYS[5]: VALUES[5],
         KEYS[6]: VALUES[6],
         KEYS[7]: VALUES[7],

    }

    container.create_item(new_item)

def PRINTING_SINGLE_ITEM():
    existing_item = container.read_item(
        item='L28920MH1919PLC000567',
        partition_key="section1",
    )
    print("KEYS             VALUES")
    for i in range(7):
        print(list(existing_item.keys())[i],"             ",list(existing_item.values())[i])
    


