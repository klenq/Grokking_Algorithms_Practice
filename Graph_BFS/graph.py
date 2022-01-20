# @Time : 1/16/2022 10:33 PM
# @Author : klenq
# @File : graph.py
# @Software : PyCharm

graph = {}

graph["you"] = ['alice', 'bob', 'claire']
print(graph)

graph["bob"] = ['anuj', 'peggy']
graph["alice"] = ["peggy"]
graph["claire"] = ['thom', 'jonny']
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print(graph)