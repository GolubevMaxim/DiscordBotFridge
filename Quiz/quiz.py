import asyncio
import discord
from discord.utils import get


async def answer_checker(message: discord.Message):
    channel_name = message.channel.name

    if channel_name.startswith("уровень-"):
        lvl = int(channel_name.split("-")[1])
        must_have_role = f"{lvl} уровень"

        if must_have_role in [give_role.name for give_role in message.author.roles]:
            with open("Quiz/answers.txt", "r", encoding="utf-16") as ans_file:
                ans = ""
                for _ in range(lvl):
                    ans = ans_file.readline()
                if message.content.strip() == ans.strip():
                    await message.channel.send(f"you got dem wright!!! go to lvl {lvl + 1}")

                    old_lvl = get(message.guild.roles, name=must_have_role)
                    new_lvl = get(message.guild.roles, name=must_have_role.replace(str(lvl), str(lvl + 1)))

                    await message.author.remove_roles(old_lvl)
                    await message.author.add_roles(new_lvl)
                else:
                    response = await message.channel.send("Wrong answer LOSER!) try again")
                    await asyncio.sleep(3)
                    await response.delete()
        else:
            response = await message.channel.send(f"you must have role: {must_have_role}")
            await asyncio.sleep(3)
            await response.delete()

        await message.delete()
