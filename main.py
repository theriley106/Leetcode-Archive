import requests
import bs4
import removeComments
import ast, astunparse
import sys
import os

def get_question():
	# Example URL: https://leetcode.com/submissions/detail/365778560/
	return bs4.BeautifulSoup(open("response.html").read(), 'lxml')

def remove_comments(fileName):
	e = []
	with open(fileName) as f:
		lines = astunparse.unparse(ast.parse(f.read())).split('\n')
		for line in lines:
			if line.lstrip()[:1] not in ("'", '"'):
				e.append(line.replace("class Solution(object, ):", "class Solution(object):"))
	return '\n'.join(e)

def get_code_for_question(page):
	print page.title.string
	question = str(page).partition("submissionCode: '")[2].partition("editCodeUrl")[0][::-1].partition("'")[2][::-1]
	return question.decode('unicode_escape').replace('\\', '')

if __name__ == '__main__':
	# print 
	page = get_question()
	with open("tmp", "w") as text_file:
		text_file.write(get_code_for_question(page))
	with open("tmp2.py", "w") as text_file:
		text_file.write(remove_comments("tmp").strip())
	fileName = str(page.title.string).replace(" ", "-").partition("---")[0]
	os.system("autopep8 tmp2.py --in-place")
	os.system("carbon-now tmp2.py -t screenshots/{}".format(fileName))
	os.system("mv tmp2.py code/{}.py".format(fileName))
