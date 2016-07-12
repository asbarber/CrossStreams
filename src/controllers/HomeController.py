from src.controllers.BaseController import BaseController

class HomeController(BaseController):
	def get(self):
		self.render("index_http.html")
