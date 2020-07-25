# -*- coding: utf-8 -*-
import requests
import bs4
import removeComments
import ast, astunparse
import sys
import os
import datetime
import sys  

reload(sys)  
sys.setdefaultencoding('utf-8')

def convert_date(relative):
    #using simplistic year (no leap months are 30 days long.
    #WARNING: 12 months != 1 year
    if 'minutes' in relative:
    	return datetime.datetime.today().strftime('%B %Y')
    unit_mapping = [('mic', 'microseconds', 1),
                    ('millis', 'microseconds', 1000),
                    ('sec', 'seconds', 1),
                    ('day', 'days', 1),
                    ('weeks', 'days', 7),
                    ('mon', 'days', 30),
                    ('year', 'days', 365)]
    try:
        tokens = relative.lower().split(' ')
        past = False
        if tokens[-1] == 'ago':
            past = True
            tokens =  tokens[:-1]
        elif tokens[0] == 'in':
            tokens = tokens[1:]


        units = dict(days = 0, seconds = 0, microseconds = 0)
        #we should always get pairs, if not we let this die and throw an exception
        print tokens
        while len(tokens) > 0:
            value = tokens.pop(0)
            if value == 'and':    #just skip this token
                continue
            else:
                value = float(value)

            unit = tokens.pop(0)
            for match, time_unit, time_constant in unit_mapping:
                if unit.startswith(match):
                    units[time_unit] += value * time_constant
        return (datetime.datetime.today() - datetime.timedelta(**units)).strftime('%B %Y')

    except Exception as e:
    	print relative
        raise ValueError("Don't know how to parse %s: %s" % (relative, e))

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
	x = page.select("#result_date")[0].getText().replace(",", " and")
	x = str(x).replace('\xc2\xa0', ' ')
	date = convert_date(x)
	print date
	question = str(page).partition("submissionCode: '")[2].partition("editCodeUrl")[0][::-1].partition("'")[2][::-1]
	return question.decode('unicode_escape').replace('\\', '')

if __name__ == '__main__':
	# print 
	page = get_question()
	with open("tmp", "w") as text_file:
		text_file.write(get_code_for_question(page))
	with open("tmp2.py", "w") as text_file:
		text_file.write(remove_comments("tmp").strip())
	title = str(page.title.string)
	if title[0] == "(":
		title = title.partition(" ")[2]
	fileName = title.replace(" ", "-").partition("---")[0]
	os.system("autopep8 tmp2.py --in-place")
	os.system("carbon-now tmp2.py -t screenshots/{}".format(fileName))
	os.system("mv tmp2.py code/{}.py".format(fileName))
