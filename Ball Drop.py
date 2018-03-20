import numpy as ny
def ball_drop(h):
    g = 9.81
    time = (2*h/g)**0.5
    velocity = (2*g*h)**0.5
    print('A ball dropped from a height of {}m will take {} seconds to hit the ground.'.format(h,round(time,2)))
    print('It will travel at max velocity of {} metres per second.'.format(round(velocity,2)))
ball_drop(20)
