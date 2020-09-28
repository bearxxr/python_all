# Celery的一些配置
BROKER_URL = 'redis://localhost:6379/2'  # Broker配置，使用Redis作为消息中间件
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  # BACKEND配置，这里使用redis保留结果
CELERY_RESULT_SERIALIZER = 'json'  # 结果序列化方案
CELERY_TIMEZONE = 'Asia/Shanghai'
