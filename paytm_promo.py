from selenium import webdriver
import time
import random

print '------- Program Started -------'
print 'Opening Browser ...'

driver = webdriver.Firefox()
driver.get("https://www.paytm.com/recharge")
raw_input("Please login to your paytm account manually and then press enter here.")
loops = int(raw_input("Number of loops for this program = "))

print '------------------------------------------'
print ''

for i in range(0,loops):
	print 'Initiating Transaction Number : '+str(i+1)
	driver.get("https://www.paytm.com/recharge")

	mobile_class = driver.find_element_by_class_name("_3_cL")
	mobile_number = mobile_class.find_element_by_tag_name("input")
	mobile_number.clear()
	mobile_number.send_keys("9999999999") # Mobile Number
	print '-- Waiting 20seconds for Paytm to load mobile number details --'
	time.sleep(20)

	amount_parent_class = driver.find_element_by_class_name("_1dGv")
	amount_sub_class = amount_parent_class.find_element_by_class_name("_3_cL")
	amount = amount_sub_class.find_element_by_tag_name("input")
	amount.clear()
	amount.send_keys("10")

	button_class = driver.find_element_by_class_name("_3BxH")
	button = button_class.find_element_by_tag_name("button")
	button_text = button.text

	if button_text.upper() == 'PROCEED TO PAY BILL':
		button.click()
		print '-- Waiting 10seconds before applying promocode --'
		time.sleep(10)

		promocode_class = driver.find_element_by_class_name("pjke")
		promocode = promocode_class.find_element_by_tag_name("a")
		promocode.click()
		time.sleep(5)

		get5_class = driver.find_element_by_class_name("XQyr")
		get5 = get5_class.find_element_by_tag_name("input")
		get5.clear()
		get5.send_keys("GET5")	# Promo Code
		get5_button = get5_class.find_element_by_tag_name("button")
		get5_button.click()
		print 'Promocode applied !'
		print '-- Waiting 5 seconds before initiating payment --'
		time.sleep(5)

		payment_class = driver.find_element_by_class_name("_1x8H")
		payment = payment_class.find_element_by_tag_name("button")
		print 'Payment Initiated ...'
		payment.click()
		print 'Payment Completed !'
		if i+1 != loops:
			sleep_time = random.randint(30,60)
			print '-- Waiting '+str(sleep_time)+'seconds before initiating next transaction --'
			#Its good to wait for sometime, otherwise paytm systems might detect abnormality in transactions
			time.sleep(sleep_time)
		else:
			time.sleep(5)
		print '------------------------------------------'
	else:
		print '---- Error ----'
		print 'The checkbox is automatically selected as Y and will not allow to enter promocode'
		continue_loop = raw_input("Do you want to continue to next loop(Y/N) ?")
		if continue_loop!='Y':
			break

close_browser = raw_input("Do you want to close browser(Y/N) ?")
if close_browser !='N':
	print 'Browser will close in next 5 seconds ...'
	time.sleep(5)
	print '-- Closing Driver --'
	driver.close()
print '-- Program Completed --'