import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_token():
    return os.getenv("DISCORD_TOKEN")

def get_channel_name():
    return os.getenv("BOT_CHANNEL_NAME")

def get_messages():
    """
    assets/message.json 파일에서 메시지 목록을 불러오는 함수
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 루트 디렉터리
    MESSAGE_PATH = os.path.join(BASE_DIR, "assets", "message.json") # 메시지 경로
    with open(MESSAGE_PATH, encoding="utf-8") as f:
        MESSAGES = json.load(f)
    return MESSAGES

