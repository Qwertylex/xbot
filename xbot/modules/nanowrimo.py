import util
from pubsub import pub

import urllib2
import StringIO
import lxml
import re

def nano_wordcount(bot, args):
    if len(args) == 2:
        bot._debug("Grabbing wchistory/%s XML" % args[1])
        url = "http://nanowrimo.org/wordcount_api/wchistory/%s" % args[1]
        rawxml = urllib2.urlopen(url, timeout = 5).read().encode('utf8')
        bot._debug("xml tree: %s" % rawxml)
        doc = lxml.etree.XML(rawxml)
        if doc.xpath('error'):
            util.answer(bot, "Error: %s" % doc.xpath('error')[0].text)
        else:
            wordcount = float(doc.xpath('user_wordcount')[0].text)
            bot._debug("Word count: %d" % wordcount)
            percentage = (wordcount / 50000) * 100
            bot._debug("Percentage: %d" % percentage)
            days = doc.xpath('wordcounts')[0]
            bot._debug("Length of days list: %d" % len(days))
            today = int(days[-1][0].text)
            bot._debug("Word count for today: %d" % today)
            # this is commented out because man it doesn't work properly
            #util.answer(bot, "Word count for %s: %s (%d%% of 50K)\n%s has written %d words today." % (args[1], int(wordcount), percentage, args[1], today))
            util.answer(bot, "Word count for %s: %s (%d%% of 50K)\n" % (args[1], int(wordcount), percentage))
    else:
        util.give_help(bot, args[0], "<NaNoWriMo.org username>")

util.register(nano_wordcount, "common", "wc")

def write(bot, args):
    responses = [
        "Only if you do!",
        "After you get 100 more words~~~",
        "Talk less, write more!"
    ]
    util.answer(bot, __import__('random').choice(responses))

util.register(write, "common", "write")

def write_scan(bot):
    if re.search('edit', bot.remote['message'].lower()):
        bot._debug('Edit!')
        util.answer(bot, "\x01ACTION licks %s's face\x01" % bot.remote['nick'])

#uncomment to make the bot lick people when they say 'edit'
#pub.subscribe(write_scan, 'scanner')
