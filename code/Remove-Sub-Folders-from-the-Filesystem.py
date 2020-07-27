import re


class Solution(object):

    def removeSubfolders(self, folder):
        db = {}

        def fill_dict(val, spot):
            if (len(val) == 0):
                return {}
            spot[val[0]] = spot.get(val[0], {})
            spot[val[0]] = fill_dict(val[1:], spot[val[0]])
            return spot
        for val in folder:
            v = val.split('/')[1:]
            db[v[0]] = db.get(v[0], {})
            fill_dict(v[1:], db[v[0]])

        def del_dict(val, spot):
            if ((len(val) == 0) or (val[0] not in spot)):
                return {}
            spot[val[0]] = del_dict(val[1:], spot[val[0]])
            return spot
        a = []
        for val in folder:
            v = val.split('/')[1:]
            db[v[0]] = del_dict(v[1:], db[v[0]])

        def get_all_possible(val, dictVal, prev=[]):
            if (len(dictVal.get(val, [])) == 0):
                a.append(('/' + '/'.join((prev + [val]))))
                return
            for value in dictVal.get(val, {}).keys():
                get_all_possible(value, dictVal[val], (prev + [val]))
        for val in db.keys():
            get_all_possible(val, db)
        return a
