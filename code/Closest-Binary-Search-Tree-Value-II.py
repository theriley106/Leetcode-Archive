class Solution(object):

    def closestKValues(self, root, target, k):
        closestVals = []

        def check_val(number):
            if (len(closestVals) < k):
                return True
            return (closestVals[(-1)]['distance'] > abs((target - number)))

        def insert_val(number):
            val = {'val': number, 'distance': abs((target - number))}
            insertAt = 0
            index = (-1)
            if (len(closestVals) == 0):
                closestVals.append(val)
            else:
                index = 0
                for info in closestVals:
                    if (info['distance'] < val['distance']):
                        index += 1
                    else:
                        break
                closestVals.insert(index, val)
                while (len(closestVals) > k):
                    closestVals.pop((-1))

        def traverse(root):
            if (root == None):
                return
            if check_val(root.val):
                insert_val(root.val)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return [x['val'] for x in closestVals]