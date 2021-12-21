import discord

from discord.ext import commands


class WarnCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["w"])
    @commands.has_role("All Mighty")
    async def warn(self, ctx, member: discord.Member = None):
        if member is None:
            embed = discord.Embed(
                title='Пример использования warn',
                description="""/warn @bad_user - выдаст предупреждение
    
                /warn /w - аналогичные команды(делают одно и тоже)""",
                colour=discord.Colour.from_rgb(106, 192, 245)
            )

            await ctx.send(embed=embed)
            return

        file_info = ""
        num_of_warns = 0
        with open("Warns/warn_list.txt", "r", encoding="utf-16") as warns:
            was_in_warn_list = False
            for string in warns:
                user, num = map(int, string.split())
                if user == member.id:
                    file_info += f"{user} {num + 1}\n"
                    was_in_warn_list = True
                    num_of_warns = num + 1
                else:
                    file_info += string

        if not was_in_warn_list:
            file_info += f"{member.id} 1\n"
            num_of_warns = 1

        with open("Warns/warn_list.txt", "w", encoding="utf-16") as file:
            file.write(file_info)

        await self.punish(ctx, member, num_of_warns)

    @commands.command(aliases=["wr"])
    @commands.has_role("All Mighty")
    async def remove_warns(self, ctx, member: discord.Member = None, n: int = None):
        if member is None:
            embed = discord.Embed(
                title='Пример использования remove_warns',
                description="""/remove_warns @good_user - снимет все предупреждения
                /remove_warns @good_user 2 - снимет 2 предупреждения
    
                /remove_warns /rw - аналогичные команды(делают одно и тоже)""",
                colour=discord.Colour.from_rgb(106, 192, 245)
            )

            await ctx.send(embed=embed)
            return

        file_info = ""

        with open("Warns/warn_list.txt", "r", encoding="utf-16") as warns:
            for string in warns:
                user, num = map(int, string.split())
                if user == member.id:
                    if n is not None:
                        file_info += f"{user} {max(num - n, 0)}\n"
                else:
                    file_info += string
        with open("Warns/warn_list.txt", "w", encoding="utf-16") as file:
            file.write(file_info)

    @commands.command(aliases=["wl"])
    @commands.has_role("All Mighty")
    async def warn_list(self, ctx):
        with open("Warns/warn_list.txt", "r", encoding="utf-16") as warn_list_file:
            description = ""
            for member_warns in warn_list_file:
                if int(member_warns.split()[1]):
                    description += "<@" + member_warns.split()[0] + "> " + member_warns.split()[1] + "\n"
            embed = discord.Embed(
                title='Warn list',
                description=description,
                colour=discord.Colour.from_rgb(106, 192, 245)
            )
            await ctx.send(embed=embed)

    async def punish(self, ctx, member, warns):
        if warns == 2:
            await ctx.send("oh shit 2 warns == mute for 6 hours")
            await ctx.invoke(self.bot.get_command("mute"), member=member, delay="6h")
        if warns == 3:
            await ctx.send("oh shit 3 warns == permanent mute")
            await ctx.invoke(self.bot.get_command("mute"), member=member)


def setup(bot):
    bot.add_cog(WarnCog(bot))
