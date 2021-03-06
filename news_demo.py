import random
import requests
import xmltodict
import pprint

from bs4 import BeautifulSoup
from collections import namedtuple
from urllib.request import urlopen


Article = namedtuple("Article", "title link")

# Engineering articles
NETFLIX_ENGINEERING = "https://netflixtechblog.com"
UBER_ENGINEERING = "https://eng.uber.com"
YELP_ENGINEERING = "https://engineeringblog.yelp.com/"
META_ENGINEERING = "https://engineering.fb.com/feed/"
DATABRICKS = "https://databricks.com/blog/category/engineering"
AMAZON_DATABASES = "https://aws.amazon.com/blogs/database/"



# Finance articles
FINANCIAL_SAMURAI = "https://www.financialsamurai.com/"
FOUR_PILLAR_FINANCE = "https://fourpillarfreedom.com"
WALLET_HACKS_FINANCE = "https://wallethacks.com/blog/"

# Health Articles
MELLOWED = "https://mellowed.com/"
MIND_BODY_GREEN = "https://www.mindbodygreen.com"

# Productivity/Lifestype articles
BENJAMIN_HARDY = "https://benjaminhardy.com/articles/"
BE_MORE_WITH_LESS = "https://bemorewithless.com/archives/"
MARK_MANSON = "https://markmanson.net/archive"
N_PRODUCTIVITY = "https://www.ntaskmanager.com/blog/category/productivity/"
THE_MANUAL = "https://www.themanual.com"

def get_netflix_articles():
    articles = []
    page = requests.get(NETFLIX_ENGINEERING)
    soup = BeautifulSoup(page.content, "html.parser")
    articles_container = soup.find_all("div", class_="u-marginBottom40 js-collectionStream")[0]
    articles_sections = []
    for article_section in articles_container.find_all("div", class_="streamItem streamItem--section js-streamItem"):
        articles_sections.append(article_section)
    for section in articles_sections:
        for element in section.find_all("a"):
            if element.has_attr("data-post-id"):
                articles.append(
                    Article(
                        title=element.find_all("div")[0].text,
                        link=element["href"]
                    )
                )
    return articles[0:3]

def get_uber_articles():
    articles = []
    page = requests.get(UBER_ENGINEERING, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, "html.parser")

    article_links = soup.find_all("a", {"rel": "bookmark"})
    for article in article_links:
        articles.append(
            Article(
                title=article.text,
                link=article["href"]
            )
        )
    return articles[0:3]


def get_financial_samurai_articles():
    articles = []
    page = requests.get(FINANCIAL_SAMURAI, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, "html.parser")
    articles_section = soup.find_all("section", id="featured-post-2")[0]
    articles_container = articles_section.find_all("div", class_="widget-wrap")[0]

    for article in articles_container.find_all("article"):
        articles.append(
            Article(
                title=article.find_all("h2")[0].text,
                link=article.find_all("h2")[0].find_all("a")[0]["href"]
            )
        )
    return articles[0:3]

def get_four_pillars_articles():
    articles = []
    page = requests.get(FOUR_PILLAR_FINANCE, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, "html.parser")
    articles_section = soup.find_all("div", id="post-wrapper")[0]
    for article in articles_section.find_all("article"):
        article = article.find_all("a", {"rel": "bookmark"})[0]
        articles.append(
            Article(
                title=article.text,
                link=article["href"]
            )
        )
    return articles[0:3]

def get_wallet_hacks_articles():
    articles = []
    page = requests.get(WALLET_HACKS_FINANCE, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, "html.parser")
    articles_section = soup.find_all("div", class_="archive-post-listing")[0]
    for article in articles_section.find_all("article"):
        article = article.find_all("a")[1]
        articles.append(
            Article(
                title=article.text,
                link=article["href"]
            )
        )
    return articles[0:3]

def get_mind_body_green_articles():
    articles = []
    CATEGORY_URLS = [
        f"{MIND_BODY_GREEN}/health/page/1",
        f"{MIND_BODY_GREEN}/food/page/1"
    ]
    
    for category_url in CATEGORY_URLS:
        page = requests.get(category_url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(page.content, "html.parser")
        articles_section = soup.find_all("section", class_="search-results")[0]
        for article in articles_section.find_all("h2", class_="search-result__heading"):
            article_route = article.find_all("a")[0]["href"]
            articles.append(
                Article(
                    title=article.find_all("a")[0].text,
                    link=f"https://www.mindbodygreen.com/articles{article_route}"
                )
            )
    return articles[0:7]

def get_mellowed_articles():
    articles_to_return = []
    page = requests.get(MELLOWED, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, "html.parser")
    articles = soup.find_all("article", class_="latestPost excerpt")
    for article in articles:
        article_anchor_tag = article.find_all("a")[0]
        articles_to_return.append(
            Article(
                title=article_anchor_tag["title"],
                link=article_anchor_tag["href"]
            )
        )
    return articles_to_return[0:7]

def get_benjamin_hardy_articles():
    articles = []
    page = requests.get(BENJAMIN_HARDY, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, "html.parser")
    articles_list_items = soup.find_all("li")
    for article in articles_list_items:
        a_tags = article.find_all("a")
        if not a_tags:
            continue
        articles.append(
            Article(
                title=a_tags[0].text,
                link=a_tags[0]["href"]
            )
        )
    return articles[0:2]

def get_be_more_with_less_articles():
    articles = []
    page = requests.get(BE_MORE_WITH_LESS, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, "html.parser")
    articles_list_items = soup.find_all("li")
    for article in articles_list_items:
        a_tags = article.find_all("a")
        if not a_tags:
            continue
        articles.append(
            Article(
                title=a_tags[0].text,
                link=a_tags[0]["href"]
            )
        )
    return articles[0:7]    


def get_mark_manson_articles():
    articles = []
    page = requests.get(MARK_MANSON, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, "html.parser")
    articles_table_data = soup.find_all("td")
    for article in articles_table_data:
        a_tags = article.find_all("a")
        if not a_tags:
            continue
        articles.append(
            Article(
                title=a_tags[0].text,
                link=f'https://markmanson.net{a_tags[0]["href"]}'
            )
        )
    return articles[0:3]

def get_n_productivity_articles():
    articles = []
    page = requests.get(N_PRODUCTIVITY, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, "html.parser")

    post_articles = soup.find_all("div", class_='post')
    for article in post_articles:
        article_link = article.find_all("a")[0]["href"]
        if (article.find_all("h3")):
            article_title = article.find_all("h3")[0].text
        else:
            article_title = article.find_all("p")[0].text
        articles.append(
            Article(
                title=article_title,
                link=article_link
            )
        )
    return articles[0:4] 


def get_the_manual_articles():
    articles = []
    page = requests.get(THE_MANUAL, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, "html.parser")
    post_articles = soup.find_all("a", class_='b-snippet__hot')
    for article in post_articles:
        articles.append(
            Article(
                title=article.text,
                link=article["href"]
            )
        )
    return articles[0:2] 


def get_yelp_articles():
    articles = []
    page = requests.get(YELP_ENGINEERING, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, "html.parser")
    all_posts = soup.find_all("div", class_="posts")[0].find_all("article")
    for article in all_posts:
        article_link = article.find_all("a")[0]["href"]
        articles.append(
            Article(
                link=f"{YELP_ENGINEERING}/{article_link}",
                title=article.find_all("a")[0].text
            )   
        )
    return articles[0:5]

def get_meta_articles():
    articles = []
    file = urlopen(META_ENGINEERING)
    data = file.read()
    file.close()

    data = xmltodict.parse(data)["rss"]["channel"]
    for key, value in data.items():
        if key == "item":
            site_data = value
            for item in site_data:
                articles.append(
                    Article(
                        title=item["title"],
                        link=item["link"]
                    )
                )
    return articles[0:5]

def get_databricks_articles():
    articles = []
    page = requests.get(DATABRICKS, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, "html.parser")
    all_posts = soup.find_all("div", class_="blog-content")[0].find_all("h2", class_="blog-post--header--title")
    for post in all_posts:
        a_tag = post.find_all("a")[0]
        articles.append(
            Article(
                title=a_tag.text,
                link=a_tag["href"]
            )
        )
    return articles[0:5]


def get_amazon_databases_articles():
    articles = []
    page = requests.get(AMAZON_DATABASES, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, "html.parser")
    all_posts = soup.find_all("article", class_="blog-post")
    for post in all_posts:
        a_tag = post.find_all("h2", class_="blog-post-title")[0].find_all("a")[0]
        articles.append(
            Article(
                title=a_tag.text,
                link=a_tag["href"]
            )
        )
    return articles



print("Starting to scrape..")
uber_articles = get_uber_articles()
netflix_articles = get_netflix_articles()
financial_samurai_articles = get_financial_samurai_articles()
four_pillar_articles = get_four_pillars_articles()
wallet_hacks_articles = get_wallet_hacks_articles()
mind_body_green_articles = get_mind_body_green_articles()
mellowed_articles = get_mellowed_articles()
benjamin_hardy_articles = get_benjamin_hardy_articles()
be_more_with_less_articles = get_be_more_with_less_articles()
mark_manson_articles = get_mark_manson_articles()
n_productivity_articles = get_n_productivity_articles()
the_manual_articles = get_the_manual_articles()
yelp_articles = get_yelp_articles()
meta_articles = get_meta_articles()
databricks_articles = get_databricks_articles()
aws_db_articles = get_amazon_databases_articles()

software_engineering_articles = uber_articles + netflix_articles + yelp_articles + meta_articles + databricks_articles + aws_db_articles
finance_articles = financial_samurai_articles + four_pillar_articles + wallet_hacks_articles
health_articles = mind_body_green_articles + mellowed_articles
productivity_articles = benjamin_hardy_articles + be_more_with_less_articles + mark_manson_articles \
    + n_productivity_articles + the_manual_articles

print(f"Scraped {len(software_engineering_articles)} software engineering articles.")
print(f"Scraped {len(finance_articles)} finance articles.")
print(f"Scraped {len(health_articles)} health articles.")
print(f"Scraped {len(productivity_articles)} productivity articles.")
print("Sending Email")

email_body = "Here are all your recent articles: \n"
email_body += "\n \n \n SOFTWARE ENGINEERING \n \n \n"
for scraped_article in software_engineering_articles:
    email_body += f"{scraped_article.title} {scraped_article.link} \n"


email_body += "\n \n \n FINANCE \n \n \n"
for scraped_article in finance_articles:
    email_body += f"{scraped_article.title} {scraped_article.link} \n"

email_body += "\n \n \n HEALTH \n \n \n"
for scraped_article in health_articles:
    email_body += f"{scraped_article.title} {scraped_article.link} \n"

email_body += "\n \n \n PRODUCTIVITY \n \n \n"
for scraped_article in productivity_articles:
    email_body += f"{scraped_article.title} {scraped_article.link} \n"

email_body += "\n \n \nBookmark the ones you plan on reading later on Raindrop.io by hitting the share button!"


print("Done sending email")
print(email_body)
