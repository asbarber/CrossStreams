import tornado.websocket
import tornado.escape
import base64
import json
from src.common import Logger

MESSAGE_PART_EVENT=0
MESSAGE_PART_DATA=1

class BaseWebSocket(tornado.websocket.WebSocketHandler):
	
	# Config / IO
	# -------------------------------------------------------------------------
	def check_origin(self, origin):
		return True

	def parse_message(self, message):
		decodedJson = tornado.escape.json_decode(message)
		return (decodedJson[MESSAGE_PART_EVENT], decodedJson[MESSAGE_PART_DATA])

	def write_base64(self, data):
		self.write_message(base64.b64encode(data))
	# -------------------------------------------------------------------------


	# Events
	# -------------------------------------------------------------------------
	def open(self):
		Logger.printOpen()

	def on_message(self, message):
		Logger.printMessageReceived(message)
		content = self.parse_message(message)
		self.on_event(content[MESSAGE_PART_EVENT], content[MESSAGE_PART_DATA])

	def on_close(self):
		Logger.printClose()
	# -------------------------------------------------------------------------


	# Abstract
	# -------------------------------------------------------------------------
	def on_event(self, event, data):
		pass
	# -------------------------------------------------------------------------
