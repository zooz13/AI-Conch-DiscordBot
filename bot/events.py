from .config import get_channel_name 
from .handles.message_handler import handle_message
from .handles.channel_handler import get_or_create_channel, verify_channels

# 환경 변수
CHANNEL_NAME = get_channel_name()    # 채널 이름

# 봇 실행 이벤트 처리
def setup_bot_events(client):
    @client.event
    async def on_ready(): 
        """
        봇이 Discord 서버에 로그인하고 준비 완료되었을 때 호출
        """
        # print(f'Logged in as {client.user}')
        # 검증
        verify_channels.start(client, CHANNEL_NAME)

    @client.event
    async def on_guild_join(guild): 
        """
        봇이 새로운 서버에 추가되었을 때 호출
        서버에 지정된 텍스트 채널이 없으면 생성
        """
        await get_or_create_channel(guild, CHANNEL_NAME)

    

# 메시지 이벤트 처리
def register_message_events(client):
    @client.event   # 메시지 수신 이벤트 핸들러
    async def on_message(message):
        """
        사용자가 메시지를 보낼 때 호출
        handle_message 핸들러를 통해 메시지 처리
        """
        await handle_message(client, message, CHANNEL_NAME)