import discord

def setup_events(client, message_handler, channel_name):
    @client.event
    async def on_ready():   # 실행
        print(f'Logged in as {client.user}')

    @client.event
    async def on_guild_join(guild): # 서버에 봇이 추가되었을 때
        existing_channel = discord.utils.get(guild.text_channels, name=channel_name)
        if not existing_channel:
            await guild.create_text_channel(channel_name)

    @client.event   # 메시지 수신 이벤트 핸들러
    async def on_message(message):
        await message_handler(message)