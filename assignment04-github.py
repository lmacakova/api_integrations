import requests
from github import Github
from config import apiKeys as cfg # modules imported
 
apiKey = cfg ["aprivateonekey"] # my private key

g = Github(apiKey)

repo = g.get_repo("lmacakova/wsaa.assignments") # chosen repository

fileInfo = repo.get_contents("text.txt") # chosen file
# Chosen file
urlOfFile = fileInfo.download_url
response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile) # content of file
newContent = "Lucia"
print (newContent) # new content
gitHubResponse=repo.update_file(fileInfo.path,"Assignment4", newContent, fileInfo.sha) # commit
print (gitHubResponse) 
