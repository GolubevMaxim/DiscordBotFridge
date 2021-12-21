import discord

from discord.ext import commands


class QuizCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gm", pass_context=True)
    @commands.has_role("All Mighty")
    async def gm(self, ctx):
        description = ""
        with open("Quiz/answers.txt", "r", encoding="utf-16") as ans_file:
            for i, ans in enumerate(ans_file):
                description += f"level {i + 1}: {ans}"

            embed = discord.Embed(
                title='Уровни игры',
                description=description,
                colour=discord.Colour.from_rgb(106, 192, 245)
            )

            await ctx.send(embed=embed)

    @commands.command(aliases=["gma"])
    @commands.has_role("All Mighty")
    async def gm_add(self, ctx, msg: str = None):
        if msg is None:
            embed = discord.Embed(
                title='Пример использования gm_add',
                description="""/gm_add answer - создает новый уровень(последний) с ответом answer
    
                /gm_add /gma - аналогичные команды(делают одно и тоже)""",
                colour=discord.Colour.from_rgb(106, 192, 245)
            )

            await ctx.send(embed=embed)
            return

        with open("Quiz/answers.txt", "a", encoding="utf-16") as ans_file:
            ans_file.write(msg.strip() + "\n")

    @commands.command(aliases=["gmr"])
    @commands.has_role("All Mighty")
    async def gm_remove(self, ctx, n: int = None):
        if n is None:
            embed = discord.Embed(
                title='Пример использования gm_remove',
                description="""/gm_remove 1 - удалит 1 уровень игры
    
                что бы отобразить уоровни воспользуйтесь коммандой /gm
    
                /gm_remove /gmr - аналогичные команды(делают одно и тоже)""",
                colour=discord.Colour.from_rgb(106, 192, 245)
            )

            await ctx.send(embed=embed)
            return

        rewrite_content = ""
        answers_cnt = 0

        with open("Quiz/answers.txt", "r", encoding="utf-16") as ans_file:
            for _ in ans_file:
                answers_cnt += 1

        if n is None:
            n = answers_cnt
        n = int(n) - 1

        with open("Quiz/answers.txt", "r", encoding="utf-16") as ans_file:
            for i, ans in enumerate(ans_file):
                if i != n:
                    rewrite_content += ans

        with open("Quiz/answers.txt", "w", encoding="utf-16") as ans_file:
            ans_file.write(rewrite_content)


def setup(bot):
    bot.add_cog(QuizCog(bot))
