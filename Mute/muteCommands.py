import discord
import asyncio

from discord.ext import commands
from discord.utils import get

from utils import time_str_to_sec


class MuteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_role("All Mighty")
    @commands.command(aliases=["m"])
    async def mute(self, ctx, member: discord.Member = None, delay: str = None):
        if member is None:
            embed = discord.Embed(
                title='Пример использования mute',
                description="""/mute @bad_user 3h - выдаcт мут @bad_user на 3 часа
                /mute @bad_user - выдаcт безсрочный мут @bad_user
    
                /mute /m - аналогичные команды(делают одно и тоже)""",
                colour=discord.Colour.from_rgb(106, 192, 245)
            )

            await ctx.send(embed=embed)
            return

        mute_role = get(ctx.guild.roles, name="Mute")
        adherent_role = get(ctx.guild.roles, name="Adherent")

        await member.add_roles(mute_role)
        await member.remove_roles(adherent_role)

        if delay is not None:
            await asyncio.sleep(time_str_to_sec(delay))
            await member.remove_roles(mute_role)
            await member.add_roles(adherent_role)

    @commands.has_role("All Mighty")
    @commands.command(aliases=["mr"])
    async def mute_remove(self, ctx, member: discord.Member = None):
        if member is None:
            embed = discord.Embed(
                title='Пример использования mute_remove',
                description="""/mute_remove @good_user - снимет мут с @good_user
    
                /mute_remove /mr - аналогичные команды(делают одно и тоже)""",
                colour=discord.Colour.from_rgb(106, 192, 245)
            )

            await ctx.send(embed=embed)
            return

        mute_role = get(ctx.guild.roles, name="Mute")
        adherent_role = get(ctx.guild.roles, name="Adherent")
        await member.remove_roles(mute_role)
        await member.add_roles(adherent_role)


def setup(bot):
    bot.add_cog(MuteCog(bot))
