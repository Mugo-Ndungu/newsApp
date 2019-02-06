from flask import render_template
from app import app
from .request import get_news, get_articles

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    news_general = get_news('general')
    news_business = get_news('business')
    news_entertainment = get_news('entertainment')
    news_sports = get_news('sports')
    news_tech = get_news('technology')
    news_science = get_news('science')
    news_health = get_news('health')

    title = 'Home - Welcome to the best News App Online'

    return render_template('index.html', title = title,general=news_general, business = news_business, entertainment = news_entertainment, sports = news_sports, tech = news_tech, science = news_science, health = news_health)


@app.route('/articles/<news_id>&<int:per_page>')
def articles(news_id,per_page):
    '''
    Function that returns articles based on their newss
    '''
    # print(news_id)
    # per_page = 40
    news_news = get_articles(news_id,per_page)
    title = f'{news_id} | All Articles'
    return render_template('articles.html', title = title, name = news_id, news = news_news)