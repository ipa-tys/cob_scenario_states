#!/usr/bin/python
import roslib
roslib.load_manifest('cob_generic_states_experimental')
import rospy
import smach
import smach_ros
from simple_script_server import *  # import script
sss = simple_script_server()

class SelectNavigationGoal(smach.State):
	def __init__(self):
		smach.State.__init__(self, 
			outcomes=['selected','not_selected','failed'],
			output_keys=['base_pose'])
			
		self.goals = []
			
	def execute(self, userdata):
		# defines
		x_min = 0
		x_max = 4.0
		x_increment = 2
		y_min = -4.0
		y_max = 0.0
		y_increment = 2
		th_min = -3.14
		th_max = 3.14
		th_increment = 2*3.1414926/4
			
	
		# generate new list, if list is empty
		if len(self.goals) == 0:
			x = x_min
			y = y_min
			th = th_min
			while x <= x_max:
				while y <= y_max:
					while th <= th_max:
						pose = []
						pose.append(x) # x
						pose.append(y) # y
						pose.append(th) # th
						self.goals.append(pose)
						th += th_increment
					y += y_increment
					th = th_min
				x += x_increment
				y = y_min
				th = th_min

		print self.goals
		userdata.base_pose = self.goals.pop()
		return 'selected'