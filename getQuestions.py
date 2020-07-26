from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import time
import glob
import json
import bs4

QUESTION_SET = requests.get("https://leetcode.com/api/problems/all/").json()['stat_status_pairs']

def find_question(query):
	if 'http' in query:
		question_title = query.partition("/problems/")[2].partition("/")[0]
		for question in QUESTION_SET:
			if question['stat']['question__title_slug'] == question_title:
				return 'https://leetcode.com/problems/{}/'.format(question_title)
	else:
		for question in QUESTION_SET:
			if str(question['stat']['frontend_question_id']) == query:
				return 'https://leetcode.com/problems/{}/'.format(question['stat']['question__title_slug'])

def return_question_filename(url):
	return url.partition("/problems/")[2].partition("/")[0] + ".png"

# def go_to_question(driver, questionNum):

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
	"(KHTML, like Gecko) Chrome/15.0.87"
)
for val in json.load(open("questions.json"))["stat_status_pairs"]:
	if val['status'] == 'ac':
		print "https://leetcode.com/problems/{}/submissions/".format(val['stat']['question__title_slug'])
		# print val

def get_accepted_from_detail_page(page):
	for a in page.find_all('a', href=True):
		if "Accepted" in str(a):
			return a['href']

print get_accepted_from_detail_page(bs4.BeautifulSoup(open("page.html").read()))
quit()


if __name__ == '__main__':

	# driver = webdriver.PhantomJS(desired_capabilities=dcap)
	driver = webdriver.Chrome()
	#driver = webdriver.Firefox()
	driver.set_window_size(1720,1080)
	driver.get("https://leetcode.com/problems/positions-of-large-groups/")
	raw_input("PRESS WHEN READY")
	for i, v in enumerate(QUESTION_SET):
		try:
			if v['stat']['question__title_slug'] + '.png' not in str(glob.glob("*.png")):
				url = 'https://leetcode.com/problems/{}/'.format(v['stat']['question__title_slug'])
				driver.get(url)
				time.sleep(2)
				if 'login' in driver.current_url:
					print("PREMIUM PROBLEM")
				else:
					driver.save_screenshot('{}.png'.format(v['stat']['question__title_slug']))
				print("{}/{}".format(i, len(QUESTION_SET)))
		except Exception as exp:
			print("ERROR + {}".format(exp))
	# time.sleep(2)
	# ".description__24" + driver.page_source.partition("description__24")[2].partition(' ')[0]
	
	# driver.save_screenshot('screen.png')
	query = raw_input("Question: ")
	while len(query) > 0:
		question_url = find_question(query)
		print question_url
		query = raw_input("Question: ")