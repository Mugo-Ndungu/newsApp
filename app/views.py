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

    title = 'Home | Best News Update Site'

    return render_template('index.html',title=title, general=news_general, business = news_business, entertainment = news_entertainment, sports = news_sports, tech = news_tech, science = news_science, health = news_health)

@app.route('/articles/<source_id>&<int:per_page>')
def articles(source_id,per_page):
    '''
    Function that returns articles based on their sources
    '''

    news_source = get_articles(source_id,per_page)
    title = f'{source_id} | All Articles'
    return render_template('articles.html', title = title, name = source_id, news = news_source)