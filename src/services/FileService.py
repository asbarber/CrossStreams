import os
import binascii
import base64
import DatabaseService

# Public
# -----------------------------------------------------------------------------
def listIds():
	return map(lambda x: x["id"], DatabaseService.getFileDatabase())

def readSegment(filename, numUsers, sequenceNum):
	numBytes = getSize(filename) // numUsers	
	offset = numBytes * sequenceNum

	# Detect if the final segment
	if (sequenceNum == numUsers - 1):
		# Handle the edge case, read remaining bytes
		numBytes = getSize(filename) - offset
		return readBytes(filename, offset, numBytes)
	else:
		# Handle the common case, attempt to divide equally
		return readBytes(filename, offset, numBytes)


def getSize(filename):
	return os.stat(filename).st_size
# -----------------------------------------------------------------------------


# Private
# -----------------------------------------------------------------------------
def readBytes(filename, offset, numBytes):
	with open(filename, 'rb') as file:
		file.seek(offset)
		return file.read(numBytes)


def readByteRange(filename, start, end):
	return readBytes(filename, offset, end - start + 1)


def readFile(filename):
	with open(filename, 'rb') as file:
		return file.read()	
# -----------------------------------------------------------------------------
