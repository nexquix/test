import requests

def get_pull_request_count(username):
    url = f"https://api.github.com/search/issues?q=author:{username}+type:pr"
    response = requests.get(url)
    data = response.json()
    return data['total_count']

username = "oscarmmv"
print(f"{username} has made {get_pull_request_count(username)} pull requests.")