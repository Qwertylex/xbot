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

def slap(bot, args):
    botresponses = [
        ";__;",
        "W-what was that for?",
        "Of course I'll slap you, %s~" % bot.remote['nick'],
        "\x01ACTION slaps %s\x01" % bot.remote['nick'],
        "\x01ACTION gets slapped by %s\x01" % bot.remote['nick']
    ]

    if len(args) == 2:
        nicks = bot.inv['rooms'].get(bot.remote['receiver'])
        if nicks:
            if args[1].lower() in [nick.lower() for nick in nicks]:
                if args[1].lower() != bot.name.lower():
                    responses = [
                        "%s slaps %s with the force of a thousand flaming suns of fury" % (bot.remote['nick'], args[1]),
                        "%s slaps %s" % (bot.remote['nick'], args[1]),
                        "%s doesn't slap %s" % (bot.remote['nick'], args[1]),
                        "%s slaps %s" % (args[1], bot.remote['nick'])
                    ]
                    util.answer(bot, __import__('random').choice(responses))
                else:
                    util.answer(bot, __import__('random').choice(botresponses))
            else:
                util.answer(bot, "B-but %s isn't here!" % args[1])
        else:
            util.answer(bot, "B-baka!")
    else:
        util.answer(bot, __import__('random').choice(botresponses))

util.register(slap, "common", "slap")

def kiss(bot, args):
    botresponses = [
        "\x01ACTION kisses %s on the cheek\x01" % bot.remote['nick'],
        "\x01ACTION kisses %s\x01" % bot.remote['nick'],
        "\x01ACTION kisses %s's foot\x01" % bot.remote['nick'],
        "L-lewd!",
        "W-why would I want to do that?"
    ]

    if len(args) == 2:
        nicks = bot.inv['rooms'].get(bot.remote['receiver'])
        if nicks:
            if args[1].lower() in [nick.lower() for nick in nicks]:
                if args[1].lower() != bot.name.lower():
                    responses = [
                        "%s kisses %s on the cheek" % (bot.remote['nick'], args[1]),
                        "%s kisses %s in the lewdest way possible" % (bot.remote['nick'], args[1]),
                        "%s kisses %s's foot" % (bot.remote['nick'], args[1]),
                        "%s sneakily kisses %s on the lips before running away~~~" % (bot.remote['nick'], args[1])
                    ]
                    util.answer(bot, __import__('random').choice(responses))
                else:
                    util.answer(bot, __import__('random').choice(botresponses))
            else:
                util.answer(bot, "B-but %s isn't here!" % args[1])
        else:
            util.answer(bot, "B-baka!")
    else:
        util.answer(bot, __import__('random').choice(botresponses))

util.register(kiss, "common", "kiss")
