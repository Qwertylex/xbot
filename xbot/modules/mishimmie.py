import util
from pubsub import pub

import urllib2
from lxml import html
import re

def mishimmie(bot, args):
    if len(args) >= 2:
        url = "";
        if re.match("id:", args[1]):
            terms = re.sub('id:', '', args[1])
            url = "http://shimmie.katawa-shoujo.com/post/view/%s" % urllib2.quote(terms)
        else:
            terms = ' '.join(args[1:])
            url = "http://shimmie.katawa-shoujo.com/post/list/%s/1" % urllib2.quote(terms)
        rawres = urllib2.urlopen(url, timeout = 5)
        result = rawres.read().encode('utf8')
        doc = html.document_fromstring(result)   
        try:
            posturl = ""
            postdesc = ""
            bot._debug('URL: %s' % rawres.geturl())
            if re.search('/post/view/', rawres.geturl()):
                bot._debug('On a post page.')
                posturl = rawres.geturl()
                postdesc = doc.get_element_by_id('imgdata').xpath('form')[0].xpath('table')[0].xpath('tr')[0].xpath('td')[1].xpath('input')[0].get('value')
            else:
                bot._debug('On a search result page.')
                posturl = "http://shimmie.katawa-shoujo.com%s" % doc.find_class('thumb')[0].xpath('a')[0].get('href')
                postdesc = doc.find_class('thumb')[0].xpath('a')[0].xpath('img')[0].get('alt').partition(' // ')[0]
            posturl = re.sub('\?.*', '', posturl)
            util.answer(bot, "\x02Mishimmie:\x02 %s // %s" % (postdesc, posturl))
        except IndexError:
           util.answer(bot, "\x02Mishimmie:\x02 No results.")
    else:
        util.give_help(bot, args[0], "<query> -- search the Mishimmie for <query>")

util.register(mishimmie, "common", "mi", "mishimmie")
