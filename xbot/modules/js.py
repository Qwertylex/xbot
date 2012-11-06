import util
from pubsub import pub

from pyv8 import PyV8
from interruptingcow import timeout
import jsbeautifier
import subprocess
import urllib2
import json
import re
import os


def execute(bot, rawcmd, filters = []):
    if 'js' not in bot.inv:
        bot.inv['js'] = PyV8.JSContext()
        
        bot.inv['js'].enter()
        for j in os.listdir(os.path.join(os.path.dirname(__file__), "js")):
            if not re.match(".+\.js$", j):
                continue
            f = open(os.path.join(os.path.dirname(__file__), "js", j), 'r')
            bot.inv['js'].eval(f.read())
        bot.inv['js'].leave()
    
    botenv = json.dumps({
        'version':  bot.version,
        'users':    bot.inv['rooms'].get(bot.remote['receiver']),
        'rooms':    bot.inv['rooms'].keys(),
        'prefix':   bot.prefix,
        'caller':   bot.remote['nick']
    })
    
    command = "((function(){try {\n"
    if 'coffee' in filters:
        command += "return CoffeeScript.eval('%s')" % rawcmd
    else:
        command += "return %s" % rawcmd
    command += "\n} catch (e) { return e.toString(); } }(this)) || '').toString()"
    
    bot._debug('Entering JS context...')
    bot.inv['js'].enter()
    
    try:
        bot.inv['js'].eval("this.bot = %s" % botenv)
        with timeout(10, exception=RuntimeError):
            bot._debug('Running command...')
            result = bot.inv['js'].eval(command)
    except RuntimeError:
        bot._debug('Timeout.')
        return False
    except PyV8.JSError as e:
        bot._debug('JS error.')
        result = str(e)
    bot._debug('Ran fine.')
    
    bot._debug('Leaving JS context...')
    bot.inv['js'].leave()
    
    if result is not None:
        bot._debug('Command has result.')
        bot._debug('Converting to str...')
        result = str(result)
        bot._debug('Encoding to UTF-8...')
        result = unicode(result).encode('utf8')
        
        if re.search("^JSError:", result):
            bot._debug('Post-processing error message.')
            result = re.sub("^JSError:\\s", '', result)
            result = re.sub("\\s[(]\\s+@.+$", '', result)
        
        if 'pretty' in filters:
            result = jsbeautifier.beautify(result)
        
        return result
    else:
        bot._debug('Nothing to return.')
        return None

def js_eval(bot, callback, command, filters = []):
    result = execute(bot, command, filters)
    
    if result != None:
        if re.search('|', callback):
            options = callback.split('|')
            callback = options[0]
            options = options[1:]
        else:
            options = []
        
        pub.sendMessage("js.callback.%s" % callback, bot=bot, result=result, options=options)

pub.subscribe(js_eval, 'js.eval')

def js_run(bot, args):
    if len(args) > 1:
        if re.match(".+:$", args[1]):
            filters = re.sub(":$", '', args[1]).split(',')
            command = ' '.join(args[2:])
        else:
            filters = []
            command = ' '.join(args[1:])
        
        if 'http' in filters:
            bot._debug("Getting js from http: %s" % command)
            command = urllib2.urlopen(command, timeout = 5).read()
            filters.remove('http')
        
        if 'gist' in filters:
            bot._debug("Getting js from gist: %s" % command)
            command = urllib2.urlopen("https://raw.github.com/gist/%s" % command, timeout = 5).read()
            filters.remove('gist')
        
        result = execute(bot, command, filters)
        
        if result == False:
            util.answer(bot, "Took too long, nigga.")
            return None
        
        if result != None and len(result) > 0:
            if len(result.split('\n')) > 4 or len(result) > 200:
                bot._debug('Going to upload to sprunge...')
                service = ['curl', '-F', 'sprunge=<-', 'http://sprunge.us']
                for n in range(2):
                    p = subprocess.Popen(service, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    paste = p.communicate(input="/* >>> %s\n<<< */\n\n%s" % (command, result))[0]
                    try:
                        util.answer(bot, "%s?js" % re.findall('(http://.*)', paste, re.S)[0].strip())
                        return None
                    except IndexError:
                        pass
                util.answer(bot, "!%s: error pasting output." % args[0])
            else:
                bot._debug('Returning locally...')
                util.answer(bot, result)
    else:
        util.give_help(bot, args[0], "[FILTERS:] <expr>")
        util.answer(bot, "\tAvailable filters: pretty, coffee, http, gist.")
        util.answer(bot, "\tE.g. %s%s pretty,coffee: <coffee_expr>" % (bot.prefix, args[0]))
        util.answer(bot, "\t     %s%s http: <url>" % (bot.prefix, args[0]))
        util.answer(bot, "\t     %s%s gist: <gist_id>" % (bot.prefix, args[0]))
        

util.register(js_run, "common", "js")

def js_reset(bot, args):
    bot._debug('Destroying JS context...')
    del bot.inv['js']
    util.answer(bot, "Success: Javascript context reset.")

util.register(js_reset, "reset", "js")