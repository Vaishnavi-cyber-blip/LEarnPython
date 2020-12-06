import requests

# r =  requests.get("url name")
# Pre-requisite: internet connection
# get function gets the code content of a entered url

# Usage of post request

url = "http://creativethinkers.ezyro.com/"
data = {
    "p1": 7,
    "p2": 9
}
r2 = requests.post(url=url, data=data)

# Task : Search for free API , Send a post request to it
