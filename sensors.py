#!/usr/bin/env python
# -*- coding:utf-8 -*-

from configparser import ConfigParser
import time
from sensor_classes import *


def parse_config():
    config = ConfigParser()
    config.read('config.config')
    influxdb = config['influxdb']
    influxdb_params = {
        "url": influxdb["url"],
        "port": influxdb["port"],
        "username": influxdb["username"],
        "pwd": influxdb["password"],
        "db_name": influxdb["database"]
    }
    return influxdb_params


if __name__ == "__main__":
    logger = Logger("Magnet")
    logger.connect(backup_dir="/Users/Cosmos S/Documents/Sr Lab/logs",  **parse_config())
    sensors = [Magnetometer("Magnet", board_port="COM5", print_m=True)]
    logger.add_sensors(sensors)
    while True:
        try:
            logger.generate_body()
            logger.upload()
            time.sleep(1)
        except Exception as err:
            print(err)
            logger.disconnect
