import os
class Config:
    '''
    General configuration parent class
    '''

    NEWS_BASE_API_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey=212b0b391fb8496e859d04f7f34ed150'
    SOURCE_NEWS_URL = 'https://newsapi.org/v2/everything?language=en&category={}&apiKey=212b0b391fb8496e859d04f7f34ed150'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')



class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''

    pass


class DevConfig(Config):
    '''
    Development Configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}