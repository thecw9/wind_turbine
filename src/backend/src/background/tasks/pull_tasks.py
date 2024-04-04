from celery import Task
from src.background.celery_app import celery_app
from src.services import data_service, nrmock_service


class MyTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print("Task failed: {0!r}".format(exc))
        # self.update_state(task_id=task_id, state="FAILURE", meta={"exc": str(exc)})


import time


@celery_app.task(base=MyTask)
def pull_main_bearing():
    keys = nrmock_service.get_keys_from_nrmock_service(include=["主轴承"])
    data = nrmock_service.get_realtime_data_from_nrmock_service(keys)
    response = data_service.store_realtime_data(data)
    data = data_service.model_predict(data)
    response = data_service.store_measure_alarm_data(data)
    return {
        "status": "success",
        "message": "主轴承数据拉取成功",
    }


@celery_app.task(base=MyTask)
def pull_generator():
    keys = nrmock_service.get_keys_from_nrmock_service(include=["发电机"])
    data = nrmock_service.get_realtime_data_from_nrmock_service(keys)
    response = data_service.store_realtime_data(data)
    data = data_service.model_predict(data)
    response = data_service.store_measure_alarm_data(data)
    return {
        "status": "success",
        "message": "发电机数据拉取成功",
    }


@celery_app.task(base=MyTask)
def pull_transducer():
    keys = nrmock_service.get_keys_from_nrmock_service(include=["变频器"])
    data = nrmock_service.get_realtime_data_from_nrmock_service(keys)
    response = data_service.store_realtime_data(data)
    data = data_service.model_predict(data)
    response = data_service.store_measure_alarm_data(data)
    return {
        "status": "success",
        "message": "变频器数据拉取成功",
    }


@celery_app.task(base=MyTask)
def pull_gearbox():
    keys = nrmock_service.get_keys_from_nrmock_service(include=["齿轮箱"])
    data = nrmock_service.get_realtime_data_from_nrmock_service(keys)
    response = data_service.store_realtime_data(data)
    data = data_service.model_predict(data)
    response = data_service.store_measure_alarm_data(data)
    return {
        "status": "success",
        "message": "齿轮箱数据拉取成功",
    }


@celery_app.task(base=MyTask)
def pull_yaw():
    keys = nrmock_service.get_keys_from_nrmock_service(include=["偏航"])
    data = nrmock_service.get_realtime_data_from_nrmock_service(keys)
    response = data_service.store_realtime_data(data)
    data = data_service.model_predict(data)
    response = data_service.store_measure_alarm_data(data)
    return {
        "status": "success",
        "message": "偏航系统数据拉取成功",
    }


@celery_app.task(base=MyTask)
def pull_default():
    keys = nrmock_service.get_keys_from_nrmock_service(include=["默认变量"])
    data = nrmock_service.get_realtime_data_from_nrmock_service(keys)
    response = data_service.store_realtime_data(data)
    data = data_service.model_predict(data)
    response = data_service.store_measure_alarm_data(data)
    return {
        "status": "success",
        "message": "默认变量数据拉取成功",
    }


@celery_app.task(base=MyTask)
def diagnose_all_devices():
    device_keys = data_service.get_all_devices_keys()
    data = data_service.fusion_model_predict(device_keys)
    response = data_service.store_device_alarm_data(data)

    return {
        "status": "success",
        "message": "所有设备诊断成功",
    }
