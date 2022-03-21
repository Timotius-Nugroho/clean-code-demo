import time
from configs.connection import vehicle
from configs.CONSTANT import TARGET_ALT, AIR_SPEED, X, Y

def takeoff_breaker():
  while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if (vehicle.location.global_relative_frame.alt >= TARGET_ALT*0.95):
            print("Reached target altitude")
            break
        time.sleep(1)

def distance_converter():
  distance_result = (X**2 + Y**2)**0.5
  duration = distance_result / AIR_SPEED

  velocity_x = X / duration
  velocity_y = Y / duration

  return velocity_x, velocity_y, duration