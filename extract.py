from os import environ, mkdir, path
import xml.etree.ElementTree as ET

from dotenv import load_dotenv
import requests as req
import pandas as pd

def load_rss_feed(url):
    """Returns RSS data as an XML tree."""
    res = req.get(url)

    return ET.fromstring(res.text).find("./channel")


def extract_article_data(feed):
    """Returns a list of article detail dicts from an XML element."""
    
    holder = []

    for item in feed.findall(".//item"):

        data = {
            "title": item.find("./title").text.strip(),
            "description": item.find("./description").text.strip(),
            "link": item.find("./link").text.strip()
        }

        holder.append(data)

    return holder



if __name__ == "__main__":

    load_dotenv()

    feed_a = load_rss_feed(environ["FEED_URL_A"])
    feed_b = load_rss_feed(environ["FEED_URL_B"])

    articles_a = extract_article_data(feed_a)
    articles_b = extract_article_data(feed_b)

    for article in articles_a:
        article["source"] = "Daily Mail"
    
    for article in articles_b:
        article["source"] = "BBC"

    articles_a.extend(articles_b)
    df = pd.DataFrame(articles_a)

    if not path.exists("./data"):
        mkdir("data")

    df.to_csv("./data/articles.csv", index=False)

    