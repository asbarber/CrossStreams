from src.controllers.BaseController import BaseController
from src.resources import UserResource


# Endpoints
# -----------------------------------------------------------------------------
def listUsers(req):
	pass

def addUser(req):
	pass

def getUser(req):
	pass

def updateUser(req):
	pass

def deleteUser(req):
	pass
# -----------------------------------------------------------------------------


# Routing
# -----------------------------------------------------------------------------
class UsersController(BaseController):
	def initialize(self):
		self.GET = listUsers
		self.POST = addUser

class UserController(BaseController):
	def initialize(self):
		self.GET = getUser
		self.POST = updateUser
		self.DELETE = deleteUser
# -----------------------------------------------------------------------------		