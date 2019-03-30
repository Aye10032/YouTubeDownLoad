import requests
import webbrowser

url = 'https://api.github.com/repos/Aye10032/YouTubeDownLoad/releases/latest'

r = requests.get(url)
downloadLink = r.json()['assets'][0]['browser_download_url']
appname = r.json()['assets'][0]['name']
version = r.json()['tag_name']
print(downloadLink)
print(appname)
print(version)

link = r.json()['html_url']
webbrowser.open(link)
