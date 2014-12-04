#! /usr/bin/python
import optparse
import os

os.chdir('/Users/mac/Documents/shareknowledge/applications/chuotnhat/databases')
os.system('rm -f *')
os.chdir('/Users/mac/Documents/shareknowledge/applications/chuotnhat/sessions')
os.system('rm -f *')
os.chdir('/Users/mac/Documents/shareknowledge')
os.system("python web2py.py -a '' --port 8002")

def main():
	p = optparse.OptionParser()
  	p.add_option('--person', '-p', default="world")
      	options, arguments = p.parse_args()
       	print 'Hello %s' % options.person
      
if __name__ == '__main__':
   	main()
