import discord

from discord.ext import commands


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["fhelp", "fridgehelp"])
    async def h(self, ctx):
        description = """
        <Мут>
        /mute @user_name "time" - Мут на время
        /mute_remove @user_name - Снять мут
    
        <Роли>
        /role add|remove @role @user_name - Выдать или забрать роль
        /reaction_roles emoji1 role1 emoji2 role2 ... - создать голосование с выдачей ролей по эмоции
    
        <Предупреждения>
        /warn @user_name - Добавить одно предупреждение
        /warns_remove @user_name N - Снять N предупреждений
        /warn_list - Выводит список предупреждений
    
        <Игра>
        /gm - Выводит ответы на игру
        /gm_add answer - создает новый уровень с ответом answer
        /gm_remove N - удаляет уровень с номером N
        """

        embed = discord.Embed(
            title='Список команд',
            description=description,
            colour=discord.Colour.from_rgb(106, 192, 245)
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpCog(bot))
