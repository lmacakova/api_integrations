# wsaa.assignments
## Author: Lucia Macakova
## Web Service and Applications - Assignment tasks

### About: 
This is my solution for assignment tasks in the module Web Services and Applications. I am the only contributor.
I used modules requests[^1], json[^2], Github from PyGithub library[^3], and an authorisation token from my config.py file

##### assignment2-carddraw.py

Task: To write a program that prints out 5 cards from https://deckofcardsapi.com[^4], and to print the value and suit of each card.

Solution: From the webpage https://deckofcardsapi.com I copied a url https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1 to get a deck through requests.get(url) and printed its information as json object. Then I asked a draw for this deck with draw url https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5 through requests.get(draw_url) and printed this draw.

##### assignment3-cso.py
Task: To write a program that retrieves the dataset for the Exchequer Account (Historical Series)" from the Central Statistic Office's page [^5] , and to store it in a file called "cso.json".

Solution: First, I found the dataset Exchequer Account (Historical Series) on the webpage  https://www.cso.ie/en/index.html and copied the link for API Data Query method GET. I asked for data with request.get(cso), printed and stored it as cso.json

##### assignment4-github.py
Task:  To write a program that will read a file from a repository. The program should then replace all the instances of the text "Andrew" in txt file with my name. The program should then commit those changes and push the file back to the repository. 

Solution: I asked for the creation of an authorization token for the repository, and then saved this token in my config.py file. With repo = g.get_repo("lmacakova/wsaa.assignments") I chose the repository and with fileInfo = repo.get_contents("text.txt"), I chose the file. I downloaded the url of the file. I asked for content with fileInfo = repo.get_contents("text.txt") and printed it. Then I printed the new content of file and commit it to file with gitHubResponse=repo.update_file(fileInfo.path,"Assignment4", newContent, fileInfo.sha). I printed gitHubResponse.


### Contact:
Lucia Macakova
email: G00439449@atu.ie



### Resources:
[^1]:   https://pypi.org/project/requests/
[^2]:   https://docs.python.org/3/library/json.html   
[^3]:   https://pygithub.readthedocs.io/en/latest/introduction.html
[^4]:   https://deckofcardsapi.com
[^5]:   https://www.cso.ie/en/index.html