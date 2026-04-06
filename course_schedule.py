def canFinish(numcourses,prerequisites):
    graph={i:[] for i in range (numcourses)}
    for a,b in prerequisites:
        graph[a].append(b)
    visited=set()
    path=set()
    def dfs(course):
        if course in path:
            return False
        if course in visited:
            return True
        path.add(course)
        for pre in graph[course]:
            if not dfs(pre):
                return False
        path.remove(course)
        visited.add(course)
        return True
    for c in range(numcourses):
        if not dfs(c):
            return False
    return True
print(canFinish(2,[[1,0]]))
print(canFinish(2,[[1,0],[0,1]]))

    
