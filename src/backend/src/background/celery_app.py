from celery import Celery
from celery.schedules import crontab
from celery.signals import task_failure
from src.config import Config
from src.logger import Logger

config = Config()
logger = Logger(__name__)

celery_app = Celery(
    "tasks",
    broker=config.CELERY_BROKER_URL,
    backend=config.CELERY_RESULT_BACKEND,
    include=[
        "src.background.tasks.model_tasks",
        "src.background.tasks.pull_tasks",
    ],
)

celery_app.conf.update(
    broker_connection_retry_on_startup=True,
    timezone="Asia/Shanghai",
    enable_utc=True,
)


celery_app.conf.beat_schedule = {
    # every 1 minute
    "pull_main_bearing": {
        "task": "src.background.tasks.pull_tasks.pull_main_bearing",
        # "schedule": crontab(hour="*/1"),
        "schedule": crontab(minute="*/1"),
    },
    "pull_generator": {
        "task": "src.background.tasks.pull_tasks.pull_generator",
        "schedule": crontab(minute="*/1"),
    },
    "pull_transducer": {
        "task": "src.background.tasks.pull_tasks.pull_transducer",
        "schedule": crontab(minute="*/1"),
    },
    "pull_gearbox": {
        "task": "src.background.tasks.pull_tasks.pull_gearbox",
        "schedule": crontab(minute="*/1"),
    },
    "pull_yaw": {
        "task": "src.background.tasks.pull_tasks.pull_yaw",
        "schedule": crontab(minute="*/1"),
    },
    "pull_default": {
        "task": "src.background.tasks.pull_tasks.pull_default",
        "schedule": crontab(minute="*/1"),
    },
    "diagnose_all_devices": {
        "task": "src.background.tasks.pull_tasks.diagnose_all_devices",
        "schedule": crontab(minute="*/1"),
    },
}


celery_app.conf.update(
    broker_connection_retry_on_startup=True,
    timezone="Asia/Shanghai",
    enable_utc=True,
)


if __name__ == "__main__":
    celery_app.start()
