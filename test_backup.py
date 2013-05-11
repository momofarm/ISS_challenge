#!/usr/bin/python
import sys
import getopt
import math 
#from pudb import set_trace; set_trace()
import logging

class ISS:
	beta = 0
	yaw = 0

	def getInitialOrientation(self, parm):
		global beta
		beta = parm
		global yaw
		yaw = 0.0
		#return yaw value we set
		return yaw
	

	# not using libcall for now, maybe later
	def libCall(self):
		print "2"
		print "1"
		for i in range(1, 14):
			print 2
		sys.stdout.flush()

		#logging.basicConfig(filename='test.log', level=logging.DEBUG)		
		for i in range(0, 696):
			data_read = input()
			#pdb.set_trace()
			#logging.basicConfig(filename='test.log', level=logging.DEBUG)
			logging.info(data_read)

		sys.stdout.flush()
		pass

	def getStateAtMinute(self, min):
		print "1"
	
		logging.info('start at min %d' % min)

		alpha = (float(360) / float(92)) * min
		logging.info('alpha value is %.2f' % alpha)

		# vector to sun
		x = math.cos(beta) * math.sin(alpha) * math.cos(yaw) - math.sin(beta) * math.sin(yaw)	
		y = -math.cos(beta) * math.sin(alpha) * math.sin(yaw) - math.sin(beta) * math.cos(yaw)
		z = -math.cos(beta) * math.cos(alpha)
		
		logging.info('the x / y / z value is %.2f %.2f %.2f' % (x, y, z))
		
		#bdata = float(x) / float(math.sqrt(x**2 + y**2 + z**2))
		#bdata = float(1) / float(z) 

		logging.info('bdata is %.2f' % bdata)

		#beta_plane = math.pi / 2 - math.acos(bdata)
		beta_plane = float(float(math.acos(bdata)) / float(math.pi)) * float(360)

		#logging.info('the starting angle is:')
		#logging.info(beta_plane)
		#logging.info('\r\n')

		for j in range(0,10):
			#logging.info('the element %d is %d' % (j, beta_plane))

			if (j == 3 or j == 5 or j == 7 or j == 9):
				beta_plane_final = beta_plane
				logging.info('the element %d is %.2f' % (j, beta_plane_final))
				print('%.2f' % beta_plane_final)
			else:
				beta_plane_final = beta_plane
				logging.info('the element %d is %.2f' % (j, beta_plane_final))
				print('%.2f' % beta_plane_final)

			print "0.15"

		sys.stdout.flush()

if __name__ == "__main__":
	#main()
	
	
	#print "generating ISS module\n"
	#print input
	a = input()

	iss = ISS()
	
	logging.basicConfig(filename='test.log', level=logging.DEBUG)		
	
	#for line in input:
	y = iss.getInitialOrientation(a)
	print y
	sys.stdout.flush()

	# arbitrary call to lib method
	#iss.libCall()
	#iss.libCall2()

	#
	for j in range(0, 93):
		iss.getStateAtMinute(j)
