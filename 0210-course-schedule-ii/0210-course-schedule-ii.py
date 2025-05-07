class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        preMap={i: [] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        output=[]
        visitSet=set()
        cycleSet=set()
        def dfs(crs):
            if crs in cycleSet:
                return False
            if crs in visitSet:
                return True
            cycleSet.add(crs)
            for  pre in preMap[crs]:
                if dfs(pre)==False:
                    return False
            cycleSet.remove(crs)
            visitSet.add(crs)
            output.append(crs)
            return True
        for crs in range(numCourses):
            if dfs(crs)==False:
                return []
        return output


            
        