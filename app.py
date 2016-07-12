import tornado.ioloop
import tornado.web
import tornado.options
from src.sockets.FileSocket import FileSocket
from src.controllers.FileController import FilesController
from src.controllers.FileController import FileController
from src.controllers.FileController import FileSegmentController
from src.controllers.FileController import FileVoteController
from src.controllers.UserController import UsersController
from src.controllers.UserController import UserController
from src.controllers.HomeController import HomeController
import os


# Configuration
# -----------------------------------------------------------------------------
tornado.options.define("port", default=8888, help="run on the given port", type=int)

ROOT = os.path.dirname(__file__)
STATIC_PATH = os.path.join(ROOT, "static")
TEMPLATE_PATH = os.path.join(ROOT, "static/templates/")

ENDPOINTS =	[
	(r"/", HomeController),
	(r"/http", HomeController),

	(r"/http/files", FilesController),
	(r"/http/files/[0-9]+", FileController),
	(r"/http/files/[0-9]+/segment", FileSegmentController),
	(r"/http/files/[0-9]+/vote", FileVoteController),

	(r"/http/users", UsersController),
	(r"/http/users/[0-9]+", UserController),

	(r"/ws/files", FileSocket)
]
# -----------------------------------------------------------------------------


# Runs application
# -----------------------------------------------------------------------------
def make_app():
	return tornado.web.Application(
		ENDPOINTS,
		template_path=TEMPLATE_PATH,
		static_path=STATIC_PATH
	)

def start_app():
	tornado.options.parse_command_line()
	app = make_app()
	app.listen(tornado.options.options.port)
	tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
	start_app()
# -----------------------------------------------------------------------------
