#! /usr/bin/python
from optparse import OptionParser
import os

def execute_test(option):
	os.chdir('/Users/mac/Documents/shareknowledge/applications/chuotnhat/funtionalTest')
	#os.system('python NotLoginUser.py local')
	#os.system('python AfterLogin.py local')
	os.system('python fb_page.py ' + option)

def main():
	parser = OptionParser()
	parser.add_option("-t", "--target", dest="env",
                  help="select target to run test against: local or test_version ",default = "local",  metavar="local")
	(options, args) = parser.parse_args()
	execute_test(options.env)



      
if __name__ == '__main__':
   	main()
