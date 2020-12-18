#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pymongo

# client = pymongo.MongoClient("mongodb://localhost:27017")
client = pymongo.MongoClient()

dblist = client.list_database_names()

print(dblist)

db_test = client["test"]
collist = db_test.list_collection_names()

print(collist)
client.close()