import requests
from github import Github
from config import apiKeys as cfg 
 
apiKey = cfg ["aprivateonekey"] 

g = Github(apiKey)

repo = g.get_repo("lmacakova/wsaa.assignments") 

fileInfo = repo.get_contents("text.txt") 
# Chosen file
urlOfFile = fileInfo.download_url
response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile) 
newContent = "Lucia"
print (newContent)
gitHubResponse=repo.update_file(fileInfo.path,"Assignment4", newContent, fileInfo.sha)
print (gitHubResponse) 
