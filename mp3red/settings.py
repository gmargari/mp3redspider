# Scrapy settings for mp3red project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'mp3red'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['mp3red.spiders']
NEWSPIDER_MODULE = 'mp3red.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

