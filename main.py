"""
Not understanding what's going on? https://discordpy.readthedocs.io/en/latest/
"""
import discord, random

from discord.ext import commands
from asyncio import sleep


class Miner(commands.Bot):
    def __init__(self, number, channel, token):
        self.number = number
        self.channel = channel
        self.token = token
        super().__init__(
            command_prefix = '..',
            self_bot = True
        )

    count = 0

    def get_owner(self):
        return self.owner_id

    #Random commands, so that dank memer doesn't think we're a bot running the same commands over and over
    commands = [
        'pls use candy',
        'pls help',
        'pls dankrate',
        'pls ferret',
        'pls sell candy',
        'pls dog',
        'pls cat',
        'pls fox',
        'pls ducc',
        'pls bal',
        'pls inv'
           ]


    async def on_ready(self):
        print(f"dank-memer-miner-{self.number} online.")
        channel = self.get_channel(self.channel)

        while True:
            await channel.send('pls beg')

            await sleep(1)
            await channel.send('pls fish') #Optional, but drastically increases the earnings

            await sleep(1)
            await channel.send('pls dig')  #Optional, but drastically increases the earnings

            self.count += 1
            await sleep(44)

            if self.count%10 == 0: #Check if it's the 10th time the command was sent
                await channel.send(random.choice(self.commands))
                await sleep(120) #Bot waits for 2 minutes before sending commands again


    def run(self):
        super().run(self.token, bot=False)
