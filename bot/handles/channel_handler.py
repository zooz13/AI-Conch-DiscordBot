from discord.ext import tasks

async def get_or_create_channel(guild, channel_name):
    """
    봇이 사용할 채팅을 선택하는 함수
    채널이 없으면 -> 생성
    채널이 2개 이상 있으면 -> 첫 번째 채널 사용
    """
    channels = [c for c in guild.text_channels if c.name == channel_name]

    if not channels:
        return await guild.create_text_channel(channel_name)
    
    # 1개 이상 있으면 첫 번째 채널 반환
    return channels[0]


@tasks.loop(seconds=600)
async def verify_channels(client, CHANNEL_NAME):
    """
    주기적으로 모든 서버의 채널 존재 여부 확인
    채널이 없으면 register_enter_channel() 호출
    """
    for guild in client.guilds:
        await get_or_create_channel(guild, CHANNEL_NAME)
    # print(f'Ensured channel "{CHANNEL_NAME}" exists in guild "{guild.name}" ')
