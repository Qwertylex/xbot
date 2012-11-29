import util

def lick(bot, args):
    botresponses = [
        "L-lewd!",
        "\x01ACTION blushes\x01",
        "\x01ACTION licks %s\x01" % bot.remote['nick']
    ]

    if len(args) != 1:
        tonick = ' '.join(args[1:])
        responses = [
            "%s licks %s" % (bot.remote['nick'], tonick),
            "%s doesn't lick %s" % (bot.remote['nick'], tonick)
        ]
        util.answer(bot, __import__('random').choice(responses))
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

    if len(args) != 1:
        tonick = ' '.join(args[1:])
        responses = [
            "%s hugs %s with the force of a thousand flaming suns of fury" % (bot.remote['nick'], tonick),
            "%s hugs %s" % (bot.remote['nick'], tonick),
            "%s doesn't hug %s" % (bot.remote['nick'], tonick),
            "\x01ACTION forces %s and %s into a hug\x01" % (bot.remote['nick'], tonick)
        ]
        util.answer(bot, __import__('random').choice(responses))
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

    if len(args) != 1:
        tonick = ' '.join(args[1:])
        responses = [
            "%s slaps %s with the force of a thousand flaming suns of fury" % (bot.remote['nick'], tonick),
            "%s slaps %s" % (bot.remote['nick'], tonick),
            "%s doesn't slap %s" % (bot.remote['nick'], tonick),
            "%s slaps %s" % (tonick, bot.remote['nick'])
        ]
        util.answer(bot, __import__('random').choice(responses))
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

    if len(args) != 1:
        tonick = ' '.join(args[1:])
        responses = [
            "%s kisses %s on the cheek" % (bot.remote['nick'], tonick),
            "%s kisses %s in the lewdest way possible" % (bot.remote['nick'], tonick),
            "%s kisses %s's foot" % (bot.remote['nick'], tonick),
            "%s sneakily kisses %s on the lips before running away~~~" % (bot.remote['nick'], tonick)
        ]
        util.answer(bot, __import__('random').choice(responses))
    else:
        util.answer(bot, __import__('random').choice(botresponses))

util.register(kiss, "common", "kiss")

def evillaugh(bot, args):
    util.answer(bot, "MWAHAHAHAHA")

util.register(evillaugh, "common", "evillaugh")

def marry(bot, args):
    botresponses = [
        "\x01ACTION agrees\x01",
        "\x01ACTION refuses\x01",
        "W-why would I want to do that?"
    ]

    if len(args) != 1:
        tonick = ' '.join(args[1:])
        responses = [
            "%s marries %s" % (bot.remote['nick'], tonick),
            "%s agrees" % tonick,
            "%s refuses" % tonick,
            "\x01ACTION sets up a huge wedding for %s and %s\x01" % (bot.remote['nick'], tonick)
        ]
    else:
        util.answer(bot, __import__('random').choice(botresponses))
    
util.register(marry, "common", "marry")

def poke(bot, args):
    botresponses = [
        "B-baka!",
        "L-lewd!",
        "\x01ACTION pokes %s\x01" % bot.remote['nick']
    ]

    if len(args) != 1:
        tonick = ' '.join(args[1:])
        responses = [
            "%s pokes %s" % (bot.remote['nick'], args[1]),
            "%s doesn't poke %s" % (bot.remote['nick'], args[1])
        ]
        util.answer(bot, __import__('random').choice(responses))
    else:
        util.answer(bot, __import__('random').choice(botresponses))
    
util.register(poke, "common", "poke")

def fill(bot, args):
    botresponses = [
        "B-but jetto will never fill me!",
        "L-lewd!"
    ]

    if len(args) != 1:
        tonick = ' '.join(args[1:])
        responses = [
            "lolis~",
            "candy~",
            "a daki pillow"
        ]
        util.answer(bot, "%s fills %s with %s" % (bot.remote['nick'], tonick, __import__('random').choice(responses)))
    else:
        util.answer(bot, __import__('random').choice(botresponses))
    
util.register(fill, "common", "fill")
