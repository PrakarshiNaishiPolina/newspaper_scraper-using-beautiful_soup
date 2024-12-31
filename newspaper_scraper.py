import requests
from bs4 import BeautifulSoup

url="https://edition.cnn.com/"

response=requests.get(url)

if response.status_code==200: # check if the request was successful
    #parse the HTML content
    soup=BeautifulSoup(response.content,"html.parser")
    print(soup.h2)
    headlines=soup.find_all("h2",class_="container__title_url-text container_lead-package__title_url-text")
    print("Latest News Headlines: ")
    for idx,headline in enumerate(headlines[:10],start=1):
        headline_text = headline.get_text(strip=True)
        print(f"{idx}. {headline_text}")



    with open("headlines.txt","w",encoding="utf-8") as file:
        for headline in headlines:
            file.write(headline.get_text(strip=True)+"/n")

else:
    print(f"Failed to fetch the webpage. Status code:{response.status_code}")



