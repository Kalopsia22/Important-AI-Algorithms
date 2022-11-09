#!/usr/bin/env python
# coding: utf-8

# In[6]:


Romania_Map = {
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
    'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

stack=[]
def DFS(currentnode,destination,Romania_Map,maxdepth):
    print("The current node is: ",currentnode)
    i=0
    if currentnode==destination:
        sys.exit()
        return True
    else:
        i+=1
    if maxdepth<=0:
        return False
    for node in Romania_Map[currentnode]:
        DFS(node,destination,Romania_Map,maxdepth-1)
def iterativedfs(currentnode,destination,Romania_Map,maxdepth):
    for i in range(maxdepth):
        if DFS(currentnode,destination,Romania_Map,i):
            return True
        for node in Romania_Map[currentnode]:
            if DFS(node,destination,Romania_Map,maxdepth-1):
                return True
    return False
a=input("Enter the source: ")
b=input("Enter the destination: ")
c=int(input("Enter the maxdepth you want to search: "))
if iterativedfs(a,b,Romania_Map,c):
    print("The number of nodes traversed are: ")
    print(len(stack))
else:
    print("Node not present in depth given")

