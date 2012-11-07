import util

def lick(bot, args):
    botresponses = [
        "L-lewd!",
        "\x01ACTION blushes\x01",
        "\x01ACTION licks %s\x01" % bot.remote['nick']
    ]

    if len(args) == 2:
        nicks = bot.inv['rooms'].get(bot.remote['receiver'])
        if nicks:
            if args[1].lower() in [nick.lower() for nick in nicks]:
                if args[1].lower() != bot.name.lower():
                    responses = [
                        "%s licks %s" % (bot.remote['nick'], args[1]),
                        "%s doesn't lick %s" % (bot.remote['nick'], args[1])
                    ]  
                    util.answer(bot, __import__('random').choice(responses))
                else:
                    util.answer(bot, __import__('random').choice(botresponses))
            else:
                util.answer(bot, "B-but %s isn't here!" % args[1])
        else:
            util.answer(bot, "D-don't be l-lewd!")
    else:
        util.answer(bot, __import__('random').choice(botresponses))

util.register(lick, "common", "lick")

def hug(bot, args):
    botresponses = [
        "Only if you promise not to be lewd!",
        "\x01ACTION blushes\x01",
        "\x01ACTION hugs %s\x01" % bot.remote['nick'],
        "\x01ACTION hugs %s with the force of a thousand flaming suns of fury\x01" % bot.remote['nick']
    ]

    if len(args) == 2:
        nicks = bot.inv['rooms'].get(bot.remote['receiver'])
        if nicks:
            if args[1].lower() in [nick.lower() for nick in nicks]:
                if args[1].lower() != bot.name.lower():
                    responses = [
                        "%s hugs %s with the force of a thousand flaming suns of fury" % (bot.remote['nick'], args[1]),
                        "%s hugs %s" % (bot.remote['nick'], args[1]),
                        "%s doesn't hug %s" % (bot.remote['nick'], args[1]),
                        "\x01ACTION forces %s and %s into a hug\x01" % (bot.remote['nick'], args[1])
                    ]
                    util.answer(bot, __import__('random').choice(responses))
                else:
                    util.answer(bot, __import__('random').choice(botresponses))
            else:
                util.answer(bot, "B-but %s isn't here!" % args[1])
        else:
            util.answer(bot, "D-don't be l-lewd!")
    else:
        util.answer(bot, __import__('random').choice(botresponses))

util.register(hug, "common", "hug")

