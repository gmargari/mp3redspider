import scrapy
from selenium import webdriver

#===============================================================================
# Song
#===============================================================================
class Song(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()

#===============================================================================
# Mp3RedSpider
#===============================================================================
class Mp3RedSpider(scrapy.Spider):
    name = 'mp3red'  # spider name

    #===========================================================================
    # start_requests ()
    #===========================================================================
    def start_requests(self):
        # Initialized our headless browser
        self.browser = webdriver.PhantomJS()
        self.browser.get('http://mp3red.me')

        search_box = self.browser.find_element_by_id('search_str')
        search_box.send_keys('Iron Maiden')

        button = self.browser.find_element_by_xpath('//input[@class="button"]')
        button.click()

        current_url = self.browser.current_url
        yield scrapy.Request(current_url, callback=self.parse_song_page)

    #===========================================================================
    # parse_song_page ()
    #===========================================================================
    def parse_song_page(self, response):

        print('%s' % response.url)

        self.browser.get(response.url)

        song_divs = self.browser.find_elements_by_xpath('//div[@class="player"]')
        for song_div in song_divs:
            song_title = song_div.get_attribute('data-title')
            song_url = song_div.get_attribute('data-mp3url')

            item = Song()
            item['title'] = song_title
            item['url'] = song_url
            yield item

            print("\t%s : %s " % (song_title, song_url))

        next_page_url = self.browser.find_element_by_xpath('//a[contains(text(),"Next page")]').get_attribute('href')
        yield scrapy.Request(next_page_url, callback=self.parse_song_page)
