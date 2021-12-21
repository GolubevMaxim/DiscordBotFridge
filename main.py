# -*- coding: utf-8 -*-
from discord.ext import commands

from config import settings


token = settings['token']
prefix = settings['prefix']

bot = commands.Bot(command_prefix=prefix)

bot.load_extension("Quiz.quizCommands")
bot.load_extension("Warns.warnCommands")
bot.load_extension("Roles.roleCommands")
bot.load_extension("Mute.muteCommands")
bot.load_extension("Help.helpCommands")
bot.load_extension("Event.events")


if __name__ == "__main__":
    bot.run(token)
