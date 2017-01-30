import requests

from ircbot import bot


@bot.command('bunny')
def bunny_command(bot, channel, sender, args):
    uri = "https://api.bunnies.io/v2/loop/%s/?media=gif"
    part = "random"
    if args:
        try:
            part = str(int(args[0]))
        except ValueError:
            pass
    data = requests.get(uri % part).json()
    bot.message(channel, "https://bunnies.io/#%s - %s" % (data['id'], data['media']['gif']))
