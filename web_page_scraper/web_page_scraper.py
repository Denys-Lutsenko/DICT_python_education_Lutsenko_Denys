
import requests
from bs4 import BeautifulSoup
import string
import os


def website(target):
    return requests.get(target, headers={'Accept-Language': 'en-US,en;q=0.5'})


def art_ln(artic_ln, artic_type):
    site = website(artic_ln)
    articl_ln = []

    if site.status_code != 200:
        return site.status_code, articl_ln

    soup = BeautifulSoup(site.content, "html.parser")

    all_artic = soup.find_all("article")
    for artic in all_artic:
        curr_span = artic.find("span", {"data-test": "article.type"})
        curr_type = curr_span.find("span").text

        if curr_type == artic_type:
            main_ln = "https://www.nature.com"
            artic_ln = artic.find("a", {"data-track-action": "view article"}).get("href")
            complete_ln = main_ln + artic_ln
            articl_ln.append(complete_ln)

    return site.status_code, articl_ln


def artic_title(artic_ln):
    soup = BeautifulSoup(website(artic_ln).content, "html.parser")

    try:
        raw_title = soup.find("h1", {"class": "c-article-magazine-title"}).text
    except AttributeError:
        raw_title = soup.find("h1", {"class": "article-item__title"}).text

    table = raw_title.maketrans("", "", string.punctuation)
    title = raw_title.translate(table)
    title = title.strip().replace(" ", "_")

    return title


def artic_cont(artic_ln):
    soup = BeautifulSoup(website(artic_ln).content, "html.parser")
    try:
        artic_cont = soup.find("div", {"class": "c-article-body"}).get_text().strip()
    except AttributeError:
        artic_cont = soup.find("div", {"class": "article-item__body"}).get_text().strip()
    return artic_cont


def save_artic(artic_ln, dir_path):
    title = artic_title(artic_ln)
    article_content = artic_cont(artic_ln)

    file_name = title + ".txt"
    full_path = dir_path + "\\" + file_name
    with open(full_path, "wb") as file:
        content_in_byte = bytes(article_content, "utf-8")
        file.write(content_in_byte)

    return title


website_link = "https://www.nature.com/nature/articles"
target_page = int(input("Enter page: "))
target_type = input("Enter article type: ")

saved_article = []
for i in range(target_page):
    curr_page = str(i + 1)
    url_in = website_link + "?page=" + curr_page
    website_code, artic_ln = art_ln(url_in, target_type)

    folder_name = "Page_" + curr_page
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    if website_code == 200:
        for link in artic_ln:
            curr_path = os.getcwd() + "\\" + folder_name
            saved_title = save_artic(link, curr_path)
            saved_article.append(saved_title)

    else:
        print("Invalid URL. Status code:", website_code)

print("Saved all articles.")
