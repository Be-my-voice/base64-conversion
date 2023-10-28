import base64

file = open("base64.online.txt", "rb") 
text = file.read()
file.close()

print(text)

fh = open("video.mp4", "wb")
fh.write(base64.b64decode(text))
fh.close()