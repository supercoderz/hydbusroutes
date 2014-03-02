# Scrapy settings for busroutes project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'busroutes'

SPIDER_MODULES = ['busroutes.spiders']
NEWSPIDER_MODULE = 'busroutes.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'busroutes (+http://www.supercoderz.in)'

ITEM_PIPELINES = {
	'busroutes.pipelines.PassThroughPipeline':100
}

DOWNLOAD_TIMEOUT = 300
DOWNLOAD_DELAY = 1