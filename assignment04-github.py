import requests
from github import Github
from config import apiKeys as cfg  # Modules imported
  
apiKey = cfg ["wsaa.assignments"] # My private key
g = Github(apiKey)

repo = g.get_repo("lmacakova/wsaa.assignments") # Chosen repository
fileInfo = repo.get_contents("README.md") # Chosen file
urlOfFile = fileInfo.download_url
response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile) # Current content
newContent = "Lucia"  # New content
print (newContent)
gitHubResponse=repo.update_file(fileInfo.path,"Assignment4", newContent, fileInfo.sha)
#print (gitHubResponse) 

