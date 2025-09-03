import discord
import os
import json
from dotenv import load_dotenv
from .events import setup_events
from .message_handler import create_message_handler

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")  # 토큰
CHANNEL_NAME = os.getenv("BOT_CHANNEL_NAME")    # 채널 이름

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 루트 디렉터리
MESSAGE_PATH = os.path.join(BASE_DIR, "assets", "message.json") # 메시지
with open(MESSAGE_PATH, encoding="utf-8") as f:
    MESSAGES = json.load(f)

intents = discord.Intents.default() # 인텐트 설정
intents.message_content = True # 메시지 내용 접근 허용

client = discord.Client(intents=intents)    # 클라이언트 생성

# 핸들러 생성 및 이벤트 등록
# 메시지 핸들러
message_handler = create_message_handler(MESSAGES, client, CHANNEL_NAME)
setup_events(client, message_handler, CHANNEL_NAME)

client.run(TOKEN)