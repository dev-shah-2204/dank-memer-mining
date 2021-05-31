"""
Not understanding what's going on? https://discordpy.readthedocs.io/en/latest/
"""
import discord, random

from discord.ext import commands
from asyncio import sleep


class Miner(commands.Bot):
    def __init__(self, number, channel, token, owner_id):
        super().__init__(command_prefix = '..',
                         self_bot = True
        )
        self.number = number
        self.channel = channel
        self.token = token

    count = 0

    normal_messages = [
                   'This is a completely normal message',
                   'listen here im not a bot',
                   'i am a normal human being',
                   'it might seem im running on a loop but trust me im not',
                   'this is one of my breaks that i get every 10 minutes',
                   'nothing fishy here, keep scrolling',
                   'ayo you got a problem?',
                   'Sup <@!270904126974590976>, im not a bot'
                  ]

    #Random commands, so that dank memer... you read the comment above...
    commands = [
            'pls help',
            'pls help image',
            'pls vr',
            'pls help currency',
            'pls dankrate',
            'pls epicgamerrate',
            'pls ducc',
            'pls ferret',
            f'pls give all <@!{owner_id}>',
            'pls sell fish all',
            'pls sell rarefish all',
            'pls sell sand all',
            'pls sell laptop all',
            'pls sell exotic all',
            'pls sell jelly all',
            'pls use candy',
            'pls sell bread all',
            'pls sell alcohol all',
            'pls sell padlock all',
            'pls sell garbage all',
            'pls sell cookie all',
            'pls sell weed all'
           ] #This list also contains selling commands for items that you will get through fishing, so you don't have to do it yourself.

    #When the bot takes a break, which message should be sent
    break_message = [
                normal_messages,
                commands
    ]

    async def on_ready(self):
        print(f"dank-memer-miner-{self.number} online.")
        channel = self.get_channel(self.channel)

        while True:
            await channel.send('pls beg')
            await sleep(1)
            await channel.send('pls fish') #Optional, but drastically increases the earnings

            self.count += 1
            await sleep(50)

            if self.count%10 == 0: #Check if it's the 10th time the command was sent
                await channel.send(random.choice(random.choice(self.break_message))) #Either a message or a command from the above lists
                await sleep(300) #Bot waits for 5 minutes before sending commands again


    def run(self):
        super().run(self.token, bot = False)
