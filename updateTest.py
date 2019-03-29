import requests

url = 'https://api.github.com/repos/Aye10032/YouTubeDownLoad/releases/latest'

r = requests.get(url)
downloadLink = r.json()['assets'][0]['browser_download_url']
appname = r.json()['assets'][0]['name']
version = r.json()['tag_name']
print(downloadLink)
print(appname)
print(version)

r = requests.get(downloadLink, stream=True)
f = open(appname, "wb")
for chunk in r.iter_content(chunk_size=512):
    if chunk:
        f.write(chunk)
