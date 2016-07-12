import json


# Config
# -----------------------------------------------------------------------------
DB_FILENAME = "db.json"
DB_FILE_KEY = "files"
DB_USER_KEY = "users"
DATABASE = None
# -----------------------------------------------------------------------------


# Public
# -----------------------------------------------------------------------------
def getFileDatabase():
	return getDatabase(DB_FILE_KEY)

def getUserDatabase():
	return getDatabase(DB_USER_KEY)
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
def getDatabase(dbName):
	return getFullDatabase()[dbName]

def getFullDatabase():
	global DATABASE
	if DATABASE == None:
		DATABASE = readFullDatabase()
	return DATABASE

def readFullDatabase():
	with open(DB_FILENAME) as file:
		return json.load(file)
# -----------------------------------------------------------------------------
