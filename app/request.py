from app import app
import urllib.request,json
from .models import news
from datetime import datetime

News = news.News

api_key = app.config['NEWS_API_KEY']
news_url = app.config['NEWS_API_BASE_URL']
articles_url = app.config['EVERYTHING_SOURCE_BASE_URL']


def configure_request(app):
    global api_key, news_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    news_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['EVERYTHING_SOURCE_BASE_URL']


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = news_url.format(category,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            sources_results = process_results(news_results_list)

    return news_results


def process_results(news_list):
    '''
    Function that processes the news results and tranforms them into a list of objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns:
        new_results: A list of news objects
    '''
    source_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')

        if url:
            news_object = News(id,name,description,url,category,country)
            source_results.append(news_object)

    return source_results


def get_articles(source_id,limit):
    '''
    Function that gets articles based on the source id
    '''
    get_article_location_url = articles_url.format(source_id,limit,api_key)

    with urllib.request.urlopen(get_article_location_url) as url:
        articles_location_data = url.read()
        articles_location_response = json.loads(articles_location_data)

        articles_location_results = None

        if articles_location_response['articles']:
            articles_location_results = process_articles(articles_location_response['articles'])
    return articles_location_results

def process_articles(my_articles):
    '''
    Function that processes the json results for the articles
    '''
    article_location_list = []
    for article in my_articles:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        date_published = article.get('publishedAt')

        publishedAt = datetime(year=int(date_published[0:4]),month=int(date_published[5:7]),day=int(date_published[8:10]),hour=int(date_published[11:13]),minute=int(date_published[14:16]))

        if urlToImage:
            article_source_object = Articles(author,title,description,url,urlToImage,publishedAt)
            article_location_list.append(article_source_object)
    return article_location_list