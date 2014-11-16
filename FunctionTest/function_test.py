#! /usr/bin/python
import optparse
import os

os.chdir('/Users/mac/Documents/shareknowledge/applications/chuotnhat/funtionalTest')
#os.system('python NotLoginUser.py')
os.system('python fb_main.py')

def main():
	p = optparse.OptionParser()
  	p.add_option('--person', '-p', default="world")
      	options, arguments = p.parse_args()
       	print 'Hello %s' % options.person
      
if __name__ == '__main__':
   	main()
