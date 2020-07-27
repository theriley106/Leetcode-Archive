class Solution(object):

    def extract_email(self, stringVal):
        domain = stringVal.partition('@')[2]
        return ((stringVal.partition('@')[0].replace('.', '').split('+')[0] + '@') + domain)

    def numUniqueEmails(self, emails):
        return len(set([self.extract_email(e) for e in emails]))