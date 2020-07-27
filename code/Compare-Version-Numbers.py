class Solution(object):

    def compareVersion(self, version1, version2):
        versionTwoLevels = {}
        versionOneLevels = {}
        totalRevisions = max(version1.count('.'), version2.count('.'))
        version1 = re.findall('d+', version1)
        version2 = re.findall('d+', version2)
        for i in range((totalRevisions + 1)):
            if (len(version1) > 0):
                versionOneLevels[i] = version1.pop(0)
            else:
                versionOneLevels[i] = 0
            if (len(version2) > 0):
                versionTwoLevels[i] = version2.pop(0)
            else:
                versionTwoLevels[i] = 0
        print versionOneLevels
        print versionTwoLevels
        self.nah = False
        self.yah = False

        def compare(version=0):
            if (version not in versionOneLevels):
                return
            if (int(versionOneLevels[version]) < int(versionTwoLevels[version])):
                self.nah = True
                return
            elif (int(versionOneLevels[version]) > int(versionTwoLevels[version])):
                self.yah = True
                return
            return compare((version + 1))
        compare(0)
        if ((self.nah == False) and (self.yah == False)):
            return 0
        if self.nah:
            return (-1)
        return 1
        return 0
        print self.nah