import unittest
from .models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_news = News('Richard','Tech is great','Advanced technology improving life','https://google.com','https://google.com/images','2018-05-12T13:31:03Z')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_news.author,'Richard')
        self.assertEquals(self.new_news.title,'Tech is great')
        self.assertEquals(self.new_news.description,'Advanced technology improving life')
        self.assertEquals(self.new_news.url,'https://google.com')
        self.assertEquals(self.new_news.urlToImage,'https://google.com/images')
        self.assertEquals(self.new_news.publishedAt,'2018-05-12T13:31:03Z')


if __name__ == '__main__':
    unittest.main()