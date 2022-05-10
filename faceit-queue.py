import discord
import os
import random
from dotenv import load_dotenv

load_dotenv()

discord_token = os.environ['DISCORD_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print("WE HAVE LOGGED IN AS {0.user}".format(client))

queue_started = False
queuers = []

@client.event
async def on_message(message):
    # message.author is the user who send a message while client.user is the bot
    if message.author == client.user:
        return
    
    global queue_started
    global queuers

    msg = message.content


    if msg.startswith('!queueStart'):
        queue_started = True
        queuers = []
        await message.channel.send("QUEUE HAS STARTED!")
        # team1 = []
        # team2 = []
        # if(msg.split("!teamup")[1].startswith(" ")):
        #     msg_content_no_cmd = msg.split("!teamup ")[1]
        # elif(msg.split("!teamup")[1].startswith("2")):
        #     msg_content_no_cmd = msg.split("!teamup2 ")[1]
        # if "," in msg: 
        #     split_names = msg_content_no_cmd.split(", ")
        # else: 
        #     split_names = msg_content_no_cmd.split(" ")
        # for name in split_names:
        #     if(random.randint(0, 1)):
        #         team1.append(name)
        #     else:
        #         team2.append(name)
        #     is_not_balanced = True
        # while is_not_balanced:
        #     if ((len(team1) > len(team2) + 1) or (len(team2) > len(team1) + 1)) == False:
        #         is_not_balanced = False
        #     if(len(team1) > len(team2) + 1): 
        #         random_pop = random.randint(0, len(team1) - 1)
        #         team2.append(team1[random_pop])
        #         team1.pop(random_pop)
        #     elif(len(team2) > len(team1) + 1): 
        #         random_pop = random.randint(0, len(team2) - 1)
        #         team1.append(team2[random_pop])
        #         team2.pop(random_pop)



    if msg.startswith("!queueUp") and queue_started == True:
        if (message.author.id in queuers) == False:
            queuers.append(message.author.id)
            await message.author.send("You have been successfully added to the queue")
        if len(queuers) == 10:
            random.shuffle(queuers)
            await message.channel.send(f"Team 1: <@{queuers[0]}> | <@{queuers[1]}> | <@{queuers[2]}> | <@{queuers[3]}> | <@{queuers[4]}>")
            await message.channel.send(f"Team 2: <@{queuers[5]}> | <@{queuers[6]}> | <@{queuers[7]}> | <@{queuers[8]}> | <@{queuers[9]}>")
    elif msg.startswith("!queueUp") and queue_started == False:
        await message.channel.send("Queue hasn't started yet, please try again later.")
        # print(queuers)
        # await message.channel.send(f"{queuers[0].mention}")

    if msg.startswith("!queueCancel"):
        queue_started = False
        queuers = []
        await message.channel.send("Queue has been canceled")
        # await message.channel.send(f"team 1: {team1}\nteam 2: {team2}")

client.run(discord_token)