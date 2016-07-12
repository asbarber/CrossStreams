import tornado.web
import base64
from tornado.escape import json_encode

class BaseController(tornado.web.RequestHandler):

	def write_bas64(self, data):
		self.write(base64.b64encode(data))

	def write_json(self, data):
		self.write(json_encode(data))

	def get(self):
		if (self.GET != None):
			self.GET(self)

	def post(self):
		if (self.POST != None):
			self.POST(self)

	def delete(self):
		if (self.DELETE != None):
			self.DELETE(self)			