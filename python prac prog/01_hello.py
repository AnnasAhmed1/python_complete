import requests
from bs4 import BeautifulSoup
from requests import Session
from bs4 import BeautifulSoup as bs
 
with Session() as s:
    site = s.get("http://quotes.toscrape.com/login")
    bs_content = bs(site.content, "html.parser")
    token = bs_content.find("input", {"name":"csrf_token"})["value"]
    login_data = {"username":"admin","password":"12345", "csrf_token":token}
    s.post("https://www.facebook.com/",login_data)
    home_page = s.get("https://www.facebook.com")
    print(home_page.content)