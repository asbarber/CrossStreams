import binascii
import base64

def printResponse(message):
	print("Server sending message... ", message)

def printOpen():
	print("Server opening socket...")

def printMessageReceived(message):
	print("Server received message... ", message)

def printClose():
	print("Server closing socket...")

def printBytearrayAsHex(bytes):
	print binascii.hexlify(b)

def printBytearrayAsBase64(bytes):
	print base64.b64encode(b)