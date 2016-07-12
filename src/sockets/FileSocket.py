from src.sockets.BaseWebSocket import BaseWebSocket
from src.resources import FileResource

class FileSocket(BaseWebSocket):
	
	# Event Handling
	# -------------------------------------------------------------------------	
	def on_event(self, event, data):
		if (event == "getSegment"):
			self.write_base64(self.getSegment(data))
	# -------------------------------------------------------------------------	

	# Public
	# -------------------------------------------------------------------------	
	def getSegment(self, data):
		return FileResource.getSegment(
			data["id"], 
			data["numUsers"], 
			data["sequenceNum"]
		)
	# -------------------------------------------------------------------------	
