# 그래프
graph = [
    ("S", "A", 2),
    ("S", "B", 3),
    ("A", "C", 1),
    ("A", "D", 3),
    ("A", "B", 2),
    ("B", "E", 4),
    ("C", "D", 3),
    ("C", "E", 2),
    ("D", "F", 1),
    ("D", "G", 2),
    ("C", "J", 6),
    ("G", "I", 4),
    ("F", "I", 3),
    ("E", "H", 4),
    ("H", "J", 1),
    ("E", "J", 6),
    ("I", "J", 2),
    ("I", "T", 3),
    ("J", "T", 5)
]

# 네트워크 자동 생성기
nodes = dict()
for n1, n2, p in graph:
    if n1 not in nodes:
        nodes[n1] = {n2:p}
    else:
        nodes[n1][n2] = p

# 노드의 가중치합들 모음.
p_node = dict.fromkeys(nodes.keys())
p_node.update({"T": None}) # 종점 노드는 추가 해야함.
p_node["S"] = (0, None)    # 시작 노드는 0

# 모든 노드를 방문하기 위해
n1 = ["S"]
while n1:
    n = n1.pop(0)[0]
    for j, k in nodes[n].items():
        current_value = k+p_node[n][0]
        if p_node[j] == None:
            p_node[j] = (current_value, n)
        else:
            if p_node[j][0] > current_value: # 더 작다면 갱신
                p_node[j] = (current_value, n)

    for i in nodes[n].keys():
        if i != "T":                         # 종점 이후는 노드가 끝.
            n1.append(i)

print(f"최단경로합: {p_node['T'][0]}")
print("경로: ", end='')
dir, i = [], "T"
while True:
    if i == None:
        break
    dir.append(i)
    i = p_node[i][1]

print(' → '.join(dir[::-1]))
#print(p_node)
