import json


# Config
# -----------------------------------------------------------------------------
DB_FILENAME = "db.json"
DATABASE = None
# -----------------------------------------------------------------------------


# Public
# -----------------------------------------------------------------------------
def getId(tag):
	obj = find(lambda item: item["tag"] == tag)
	return obj["id"] if obj != None else None

def getFilename(id):
	obj = find(lambda item: item["id"] == id)
	return obj["filename"] if obj != None else None

def listIds():
	return map(lambda x: x["id"], getDatabase())
# -----------------------------------------------------------------------------


# Private
# -----------------------------------------------------------------------------
def find(acceptor):
	for obj in getDatabase():
		if acceptor(obj):
			return obj
	return None	

def findAll(acceptor):
	found = []
	for obj in getDatabase():
		if acceptor(obj):
			found.append(obj)
	return found	
# -----------------------------------------------------------------------------


# Singleton
# -----------------------------------------------------------------------------
def getDatabase():
	global DATABASE
	if DATABASE == None:
		DATABASE = readDatabase()
	return DATABASE

def readDatabase():
	objects = []
	with open(DB_FILENAME) as file:
		for obj in json.load(file):
			objects.append(obj)
	return objects
# -----------------------------------------------------------------------------
