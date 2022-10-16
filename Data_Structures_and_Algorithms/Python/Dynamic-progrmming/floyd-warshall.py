# Floyd-Warshall Algorithm is an algorithm for finding the shortest path between all the pairs of vertices in a weighted graph.

nV = 4
INF = 999

def floys_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)

def print_solution(distance):
    for i in range(nV):
        for j in range(nV):                    
            if (distance[i][j] == INF):
                print("INF", end = " ")
            else:
                print(distance[i][j], end = " ")
            print(" ")

G = [[0, 3, INF, 4],
     [2, 0,  INF, 4],
     [INF, 1, 0, INF],
     [INF, INF, 2,0]
    ]

floys_warshall(G)