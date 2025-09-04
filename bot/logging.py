import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    # -------------------------------
    # Logging 설정
    # -------------------------------
    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO) # logging.DEBUG 로 상세 로깅 가능
    logging.getLogger('discord.http').setLevel(logging.INFO)  # HTTP 요청/응답은 INFO만

    # RotatingFileHandler: 로그 파일 자동 회전
    handler = RotatingFileHandler(
        filename='discord.log',
        encoding='utf-8',
        maxBytes=32*1024*1024,  # 32MB
        backupCount=5            # 5개 파일까지 유지
    )
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(
        '[{asctime}] [{levelname:<8}] {name}: {message}',
        dt_fmt,
        style='{'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger