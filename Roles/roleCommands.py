import discord

from discord.ext import commands
from discord.utils import get
from reactionRole import ReactionRoles
from pickletHelpFunc import save_obj, load_obj
from config import settings


class RoleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reaction_roles_messages = load_obj("reaction_roles_messages") or {}

    @commands.has_role("All Mighty")
    @commands.command(aliases=["r"])
    async def role(self, ctx, option: str = None, given_role: discord.Role = None, member: discord.Member = None):
        if member is None:
            embed = discord.Embed(
                title='Пример использования role',
                description="""/role add @user @cool_role - выдаст роль @cool_role
                /role a @user @cool_role - выдаст роль @cool_role
    
                /role remove @user @cool_role - заберет роль @cool_role
                /role r @user @cool_role - заберет роль @cool_role
    
                /role /r - аналогичные команды(делают одно и тоже)""",
                colour=discord.Colour.from_rgb(106, 192, 245)
            )

            await ctx.send(embed=embed)
            return

        if given_role is None or member is None:
            return

        member = member or ctx.message.author
        if option in ["add", "a"]:
            await member.add_roles(given_role)
        if option in ["remove", "r"]:
            await member.removr_roles(given_role)

    @commands.has_role("All Mighty")
    @commands.command(aliases=["rr"])
    async def reaction_roles(self, ctx, *message):

        roles = [message[i] for i in range(len(message)) if i % 2 == 1]
        reactions = [message[i] for i in range(len(message)) if i % 2 == 0]

        if roles == [] or reactions == [] or len(roles) != len(reactions):
            embed = discord.Embed(
                title='Пример использования reaction_roles',
                description="""/reaction_roles role1 emoji1 role2 emoji2 ... - создаст голосование с выбором двух ролей
    
                /reaction_roles /rr - аналогичные команды(делают одно и тоже)""",
                colour=discord.Colour.from_rgb(106, 192, 245)
            )

            await ctx.send(embed=embed)
            return

        description = ""
        for i in range(min(len(roles), len(reactions))):
            description += f"{reactions[i]} {roles[i]} \n"

        embed = discord.Embed(
            title='Roles',
            description=description,
            colour=discord.Colour.from_rgb(106, 192, 245)
        )

        react_msg = await ctx.send(embed=embed)

        for name in reactions:
            emoji = get(ctx.guild.emojis, name=name)
            await react_msg.add_reaction(emoji or name)

        message_id = react_msg.id
        self.reaction_roles_messages[message_id] = ReactionRoles(message_id, reactions, roles)
        save_obj(self.reaction_roles_messages, "reaction_roles_messages")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id in self.reaction_roles_messages.keys():
            guild = self.bot.get_guild(id=payload.guild_id)
            user = await guild.fetch_member(payload.user_id)
            give_role = get(
                guild.roles,
                id=int(self.reaction_roles_messages[payload.message_id].get_role_by_reaction(str(payload.emoji))[3:-1])
            )
            await user.remove_roles(give_role)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        user = payload.member
        msg = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
        emoji = payload.emoji

        if user.bot:
            return

        if str(msg.channel) == "judge" and str(msg.author) == settings["bot"]:
            if str(emoji) == "✅":
                mem = await msg.guild.fetch_member(int(msg.embeds[0].description.split()[0][2:-1]))
                ctx = await self.bot.get_context(msg)
                await ctx.invoke(self.bot.get_command("warn"), member=mem)
                await msg.delete()
            if str(emoji) == "❌":
                await msg.delete()

        if msg.id in self.reaction_roles_messages.keys():
            ctx = await self.bot.get_context(msg)

            give_role = get(
                ctx.guild.roles,
                id=int(self.reaction_roles_messages[msg.id].get_role_by_reaction(str(emoji))[3:-1])
            )
            await user.add_roles(give_role)


def setup(bot):
    bot.add_cog(RoleCog(bot))
