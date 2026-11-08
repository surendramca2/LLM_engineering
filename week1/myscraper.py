from bs4 import  BeautifulSoup
import requests

# Standard headers to fetch a website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

def test():
    print("hello test")

def fetch_my_website_link(url):
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content,"html.parer")
    links = [ link.get("href") for  link in soup.find_all("a")]
    return [ link for link in links if link]


def fetch_my_website_contents(url):
    """
      Return the website tittle and contents of the website of given URL.
    """
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content,"html.parser")
    title = soup.title.string if soup.title else "No content"
     
    if soup.body:
      for irr in soup.body(["img","script","style","input"]):
       irr.decompose()
       text = soup.body.get_text(separator="\n",strip=True)
    else:
       text=""    
       return (title +"\n\n"+text)[2_000]  

