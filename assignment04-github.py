import requests
from github import Github
from config import apikey as cfg  # Modules imported
  
apikey = cfg["aprivateonekey"] 
g = Github(apikey)

repo = g.get_repo("lmacakova/aprivateone")
fileInfo = repo.get_contents("README.md")
urlOfFile = fileInfo.download_url
response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile) 
newContent = "Lucia"
print (newContent) 
gitHubResponse=repo.update_file(fileInfo.path,"Assignment4", newContent, fileInfo.sha)
print (gitHubResponse) 
