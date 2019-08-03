import requests

url = "https://api.myjson.com/bins/jub2l"

datas = {"slideNumber":1,"360Rotation":180,"slideBrightness":0.5,"animationIsPlaying":0,"dismissPresentation":0}

headers = {'Content-type': 'application/json'}

rsp = requests.put(url, json=datas, headers=headers)
