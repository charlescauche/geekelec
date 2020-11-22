#!/usr/bin/python3.7.2
# -*-coding:Utf-8 -*

"""function mailSub to register user email in a list"""

import sys


def addMail():
	"""Add the user mail to the list emails"""
	mailing_list=[]
	user_mail = input("Please enter your email: ") # User give his email address
	
	if not "@" in user_mail: #Test to verify if this is a valid email address
		print("You didn't enter a valid email address")

	else: #if email input is valid
		mailing_list.append(user_mail)
		print("Thanks, we added your address to our list")
		print("We will send you an email to validate your subsciption")
		print(mailing_list)


# Version test 
if __name__ == "__main__":
	print(sys.version)
	print("TEST FONCTION addMail")
	addMail()

