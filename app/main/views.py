from flask import render_template, request,redirect,url_for
from . import main
from ..request import get_news, get_articles

# Views
@main.route('/')
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

@main.route('/news/<source_id>')
def articles(source_id):
    '''
    Function that returns articles based on their sources
    '''

    news_source = get_articles(source_id)
    title = f'{source_id} | All Articles'
    return render_template('articles.html', title = title, name = source_id, news = news_source)