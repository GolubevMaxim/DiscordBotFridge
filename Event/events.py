import discord

from discord.ext import commands
from discord.utils import get

from utils import translit_translate
from Quiz import quiz
from config import settings, DRAG_WORDS, BAD_WORDS


def get_judge_channel(msg):
    for channel in msg.guild.channels:
        if channel.name == "judge":
            return channel


class EventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if len(message.content) == 0:
            return

        prefix = settings['prefix']
        if message.content[0] == prefix:
            return

        if message.author == self.bot.user:
            return

        await quiz.answer_checker(message)

        for word in message.content.lower().split():
            word = translit_translate(word)

            if word in BAD_WORDS:
                judge_channel = get_judge_channel(message)

                embed = discord.Embed(
                    title='СУД!!!',
                    description=f"<@{message.author.id}> in {message.channel}: {message.content}",
                    colour=discord.Colour.from_rgb(106, 192, 245)
                )

                judge_msg = await judge_channel.send(embed=embed)
                reactions = ["✅", "❌"]
                for name in reactions:
                    emoji = get(message.guild.emojis, name=name)
                    await judge_msg.add_reaction(emoji or name)
                break

            if word in DRAG_WORDS:
                await message.channel.send("Администрация сервера не поддерживает распространение и употребление "
                                           "веществ, запрещенных в Российской Федерации.")


def setup(bot):
    bot.add_cog(EventCog(bot))
