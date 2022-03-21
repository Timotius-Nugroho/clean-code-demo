from pymavlink import mavutil
import time
from configs.connection import vehicle
from configs.CONSTANT import TIMESTAMP

def send_body_velocity(x, y, z, duration):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,
        0, 0,
        mavutil.mavlink.MAV_FRAME_BODY_NED,
        0b0000111111000111,
        0, 0, 0,
        x, y, z,
        0, 0, 0,
        0, 0)
    
    number_of_hit = round(duration / TIMESTAMP)
    for _number in range(0, number_of_hit) :
        print("LAT >>", vehicle.location.global_relative_frame.lat, " || ", "LON >>", vehicle.location.global_relative_frame.lon)
        vehicle.send_mavlink(msg)
        time.sleep(TIMESTAMP)