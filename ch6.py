from collections import deque
# bfs - breadth first search

# graph
graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["an", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["an"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def is_seller(name): # seller if name ends in m
    return name[-1] == 'e'

# search if friend is seller, good basis but not working 
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = [] 
    while search_queue: # continue till queue is empty
        person = search_queue.popleft() 
        if not person in searched: 
            if is_seller(person): # checks if seller
                print(person)
                print("is seller")
                return True
        else:
            search_queue += graph[person] # otherwise adds connected friends
            searched.append(person)
    return False

# test 
result = search("you")
print(result)