import Image

def getThumbnail(filename, width, height):
	image = Image.open(filename)
	image.thumbnail(width, height)
	bytes = io.BytesIO()
	image.save(bytes, format="JPEG")
	return bytes.getvalue()
