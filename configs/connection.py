from dronekit import connect
from configs.CONSTANT import CONNECTION_STRING

vehicle = connect(CONNECTION_STRING, wait_ready=True)