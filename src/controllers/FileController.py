from src.controllers.BaseController import BaseController
from src.resources import FileResource


# Endpoints
# -----------------------------------------------------------------------------
def listFiles(req):
	req.write_json(
		FileResource.listFiles()
	)

def addFile(req):
	req.write_json(
		FileResource.addFile(
			req.get_argument("tag", None),
			req.get_argument("owner", None),
			req.get_argument("permissions", None),
			req.get_argument("description", None)
		)
	)

def getFile(req):
	req.write_json(
		FileResource.getFile(
			req.get_argument("id", None)
		)
	)

def updateFile(req):
	req.write_json(
		FileResource.updateFile(
			req.get_argument("id", None),
			req.get_argument("permissions", None),
			req.get_argument("description", None)
		)
	)

def deleteFile(req):
	req.write_json(
		FileResource.deleteFile(
			req.get_argument("id", None)
		)
	)

def getSegment(req):
	req.write_base64(
		FileResource.getSegment(
			req.get_argument("id", None),
			int(req.get_argument("numUsers", None)),
			int(req.get_argument("sequenceNum", None))
		)
	)

def vote(req):
	req.write_json(
		FileResource.vote(
			req.get_argument("id", None),
			req.get_argument("username", None),
			req.get_argument("isUpvote", None)
		)
	)
# -----------------------------------------------------------------------------


# Routing
# -----------------------------------------------------------------------------
class FilesController(BaseController):
	def initialize(self):
		self.GET = listFiles
		self.POST = addFile

class FileController(BaseController):
	def initialize(self):
		self.GET = getFile
		self.POST = updateFile
		self.DELETE = deleteFile

class FileSegmentController(BaseController):
	def initialize(self):
		self.GET = getSegment

class FileVoteController(BaseController):
	def initialize(self):
		self.POST = vote
# -----------------------------------------------------------------------------		