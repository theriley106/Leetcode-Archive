class Solution:

    def subdomainVisits(self, cpdomains):
        temp_dict = {}
        for val in cpdomains:
            num = int(val.partition(' ')[0])
            val = val.partition(' ')[2]
            splitVals = val.split('.')
            for i in range(len(splitVals)):
                string = '.'.join(splitVals[i:])
                if (string not in temp_dict):
                    temp_dict[string] = 0
                temp_dict[string] += num
        temp_list = []
        for (key, val) in temp_dict.items():
            temp_list.append('{} {}'.format(val, key))
        return temp_list