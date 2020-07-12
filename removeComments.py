import ast, astunparse
import sys



if __name__ == '__main__':
	with open(sys.argv[1]) as f:
		lines = astunparse.unparse(ast.parse(f.read())).split('\n')
		for line in lines:
			if line.lstrip()[:1] not in ("'", '"'):
				print(line.replace("class Solution(object, ):", "class Solution(object):"))