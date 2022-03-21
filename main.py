from controllers.takeoff import takeoff
from controllers.velocity import send_body_velocity
from helpers.calculator import distance_converter

# take off phase
takeoff()

# calc velocity and duration
velocity_x, velocity_y, duration = distance_converter()

# movement
send_body_velocity(velocity_x, velocity_y, 0, duration)