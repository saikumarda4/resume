from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time

# Create your views here.
def index(request):
    
	
		driver = webdriver.Chrome("F:\\z\\chromedriver_win32\\chromedriver.exe")

	driver.get('https://www.naukri.com/nlogin/login')
	time.sleep(5)
	print("Opened naukri...")

	text = driver.find_element_by_id('usernameField')
	text.send_keys('saikumarda4@gmail.com')
	print("email entered...")
	password = driver.find_element_by_id('passwordField')
	password.send_keys('sai521sai')
	print("Password entered...")

	password.submit()
	print("facebook opened")

	time.sleep(5)
	driver.get('https://www.naukri.com/mnjuser/profile?id=&altresid')

	time.sleep(5)

	link = driver.find_element_by_xpath("//a[contains(.,'Update')]")
	link.click()
	time.sleep(5)
	uploadFile = driver.find_element_by_xpath("//input[@id='attachCV']")
	uploadFile.send_keys('F:\\z\\resume-s.pdf')
	time.sleep(5)

	print("post done")
	return HttpResponse('Hello from Python!')
    #return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

