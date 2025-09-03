import random

def create_message_handler(messages, client, channel_name):
    async def handler(message):
        if message.author == client.user:
            return
        if message.channel.name != channel_name:
            return
        answer = random.choice(messages)
        await message.channel.send(answer)
    return handler