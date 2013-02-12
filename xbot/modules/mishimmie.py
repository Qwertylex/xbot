import util
from pubsub import pub

import urllib2
from lxml import html
import re

def mishimmie(bot, args):
    if len(args) >= 2:
        terms = ' '.join(args[1:])
        url = "http://shimmie.katawa-shoujo.com/post/list/%s/1" % urllib2.quote(terms)
        result = urllib2.urlopen(url, timeout = 5).read().encode('utf8')
        doc = html.document_fromstring(result)
        try:
            posturl = "http://shimmie.katawa-shoujo.com%s" % doc.find_class('thumb')[0].xpath('a')[0].get('href')
            posturl = re.sub('\?.*', '', posturl)
            postdesc = doc.find_class('thumb')[0].xpath('a')[0].xpath('img')[0].get('alt')
            util.answer(bot, "\x02Mishimmie:\x02 %s // %s" % (postdesc, posturl))
        except IndexError:
            util.answer(bot, "\x02Mishimmie:\x02 No results.")
    else:
        util.give_help(bot, args[0], "<query> -- search the Mishimmie for <query>")

util.register(mishimmie, "common", "mi", "mishimmie")
