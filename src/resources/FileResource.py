from src.services import ContentService
from src.services import FileService

def listFiles():
	return FileService.listIds()

def addFile(tag, owner, permissions, description, filepath):
	pass

def getFile(fileId):
	pass

def updateFile(fileId, permissions, description):
	pass

def deleteFile(fileId):
	pass

def getSegment(fileId, numUsers, sequenceNum):
	return FileService.readSegment(ContentService.getFilename(fileId), numUsers, sequenceNum)
	
def vote(fileId, username, isUpvote):
	pass