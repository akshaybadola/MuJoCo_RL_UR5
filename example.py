from gym_grasper.controller.MujocoController import MJ_Controller

import ipdb; ipdb.set_trace()
# create controller instance
controller = MJ_Controller()

print('1')
# Display robot information
controller.show_model_info()

# Move ee to position above the object, plot the trajectory to an image file, show a marker at the target location
print('2')
controller.move_ee([0.0, -0.6, 0.95], plot=True, marker=True)

# Move down to object
print('3')
controller.move_ee([0.0, -0.6, 0.895])

# Wait a second
print('4')
controller.stay(1000)

# Attempt grasp
print('5')
controller.grasp()

# Move up again
print('6')
controller.move_ee([0.0, -0.6, 1.0])

# Throw the object away
print('7')
controller.toss_it_from_the_ellbow()

# Wait before finishing
print('8')
controller.stay(2000)
