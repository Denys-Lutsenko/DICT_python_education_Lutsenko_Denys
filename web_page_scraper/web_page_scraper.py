import string
import requests
from bs4 import BeautifulSoup


def artic_title(artic_ln):
    soup = BeautifulSoup(website(artic_ln).content, "html.parser")

    raw_title = soup.find("h1", {"class": "c-article-magazine-title"}).text
    table = raw_title.maketrans("", "", string.punctuation + "’")
    title = raw_title.translate(table)
    title = title.strip().replace(" ", "_")

    return title


def new_artic_ln(artic_ln):
    site = website(artic_ln)
    new_artic_ln = []

    if site.status_code != 200:
        return site.status_code, new_artic_ln

    soup = BeautifulSoup(site.content, "html.parser")

    all_artic = soup.find_all("article")
    for artic in all_artic:
        artic_span = artic.find("span", {"data-test": "article.type"})
        artic_type = artic_span.find("span").text

        if artic_type == "News":
            main_ln = "https://www.nature.com"
            artic_ln = artic.find("a", {"data-track-action": "view article"}).get("href")
            complete_ln = main_ln + artic_ln
            new_artic_ln.append(complete_ln)

    return site.status_code, new_artic_ln


def website(target):
    return requests.get(target, headers={'Accept-Language': 'en-US,en;q=0.5'})



def ar_lecont(art_ln):
    soup = BeautifulSoup(website(art_ln).content, "html.parser")
    artic_content = soup.find("div", {"class": "c-article-body"}).get_text().strip()

    return artic_content


def artic(art_ln):
    title = artic_title(art_ln)
    artic_content = ar_lecont(art_ln)

    file_name = title + ".txt"
    with open(file_name, "wb") as file:
        content_in_byte = bytes(artic_content, "utf-8")
        file.write(content_in_byte)

    return title


url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"

website_code, art_ln = new_artic_ln(url)

if website_code == 200:
    save_artic = []

    for ln in art_ln:
        save_title = artic(ln)
        save_artic.append(save_title)
        print("Article downloaded:", save_title)

    print("Downloaded article: ")
    for i in range(len(save_artic)):
        print(save_artic[i])
else:
    print("Invalid URL. Status code:", website_code)