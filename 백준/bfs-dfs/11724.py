# 1 dfs
import sys
sys.setrecursionlimit(5000)


def data_input():
    node_location, line_count = map(int, input().split())
    graph = [[] for _ in range(node_location + 1)]

    #입력값 처리
    for _ in range(line_count):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    return node_location, line_count, graph


def solution():
    def dfs(start, depth):
        # 해당 노드 방문체크 한다.
        visited[start] = True

        for i in graph[start]:
            if not visited[i]:
                dfs(i, depth + 1)

    node_location, line_count, graph = data_input()
    # 방문처리 설정
    visited = [False] * (1 + node_location)
    count = 0  # 컴포넌트 그래프 개수 저장

    # 1~N번 노드를 각각돌면서
    for i in range(1, node_location + 1):
        if not visited[i]:  # 만약 i번째 노드를 방문하지 않았다면
            if not graph[i]:  # 만약 해당 정점이 연결된 그래프가 없다면
                count += 1  # 개수를 + 1
                visited[i] = True  # 방문 처리
            else:  # 연결된 그래프가 있다면
                dfs(i, 0)  # dfs탐색을 돈다.
                count += 1  # 개수를 +1

    print(count)


solution()
