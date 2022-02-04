import discord

try:
    import tokens
except ImportError:
    pass

from discord.ext import commands

class BotControl(commands.Bot):
    """
    Class to control the bot
    """
    def __init__(self, token):
        self.token = token
        super().__init__(command_prefix = '..', self_bot = True)

    async def on_ready(self):
        print('ready')
        channel = self.get_channel(827561383650525223)  # Enter your channel ID here

        while True:
            ask = input()
            await channel.send(ask)

    def  run(self):
        super().run(self.token, bot = False)


miner = BotControl(token = tokens.miner_2)  # Enter your token here
miner.run()

"""
When you run this file, a command window will open, and after it says 'ready', start typing your messages i.e. sell commands, give/gift commands etc to transfer the mining payout to your main account
"""
