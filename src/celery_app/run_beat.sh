#/bin/bash

celery -A app.celery_app beat -l info
