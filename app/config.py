class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    EVERYTHING_SOURCE_BASE_URL = 'https://newsapi.org/v2/everything?language=en&category={}&apiKey={}'



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