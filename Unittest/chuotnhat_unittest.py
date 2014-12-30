#! /usr/bin/python
import optparse
import os

os.chdir('/Users/mac/Documents/shareknowledge')
os.system('python web2py.py -S chuotnhat -M -R applications/chuotnhat/unittest/test_question_handler.py')
os.system('python web2py.py -S chuotnhat -M -R applications/chuotnhat/unittest/test_noti_handler.py')
os.system('python web2py.py -S chuotnhat -M -R applications/chuotnhat/unittest/test_user_noti_handler.py')
os.system('python web2py.py -S chuotnhat -M -R applications/chuotnhat/unittest/test_answer_handler.py')
os.system('python web2py.py -S chuotnhat -M -R applications/chuotnhat/unittest/test_user_tag_handler.py')
os.system('python web2py.py -S chuotnhat -M -R applications/chuotnhat/unittest/test_user_following_feature_handler.py')
os.system('python web2py.py -S chuotnhat -M -R applications/chuotnhat/unittest/test_default_tag_handling.py')

def main():
	p = optparse.OptionParser()
  	p.add_option('--person', '-p', default="world")
      	options, arguments = p.parse_args()
       	print 'Hello %s' % options.person
      
if __name__ == '__main__':
   	main()
