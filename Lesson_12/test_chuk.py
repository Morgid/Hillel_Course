import requests
def test_cat():
    url = "https://api.chucknorris.io/jokes/random?category={category}"
    reqest = requests.request(method="GET", url="https://api.chucknorris.io/jokes/random")
    print(reqest.json())
    pass