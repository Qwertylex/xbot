import util
import urllib2
import StringIO
from lxml import etree

def nano_wordcount(bot, args):
    if len(args) == 2:
        url = "http://nanowrimo.org/wordcount_api/wc/%s" % args[1]
        rawxml = urllib2.urlopen(url, timeout = 5).read().encode('utf8')
        doc = etree.XML(rawxml)
        if doc.xpath('error'):
            util.answer(bot, "Error: %s" % doc.xpath('error')[0].text)
        else:
            util.answer(bot, "Word count for %s: %s" % (args[1], doc.xpath('user_wordcount')[0].text))
    else:
        util.give_help(bot, args[0], "<NaNoWriMo.org username>")

util.register(nano_wordcount, "common", "wc")
