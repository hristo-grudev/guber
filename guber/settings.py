BOT_NAME = 'guber'

SPIDER_MODULES = ['guber.spiders']
NEWSPIDER_MODULE = 'guber.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'guber.pipelines.GuberPipeline': 100,

}