import discord
from .events import setup_bot_events, register_message_events
from .config import get_token
from .logging import setup_logging

# -------------------------------
# logging 설정
# -------------------------------
logger = setup_logging()
logger.info("봇 실행 시작")

# -------------------------------
# Discord Client 생성
# -------------------------------
TOKEN = get_token()  # 토큰

intents = discord.Intents.default() # 인텐트 설정
intents.message_content = True # 메시지 내용 접근 허용
client = discord.Client(intents=intents)    # 클라이언트 생성

# 핸들러 생성 및 이벤트 등록
setup_bot_events(client)
register_message_events(client)

# 실행
client.run(TOKEN, log_handler=None) # type: ignore