import random

# 환경 변수
from ..config import get_messages
MESSAGES = get_messages()

# 초기 메시지 설정
async def handle_message(client, message, channel_name):
    if message.author == client.user:
        return
    if message.channel.name != channel_name:
        return
    answer = random.choice(MESSAGES)
    await message.channel.send(answer)