# #define the graph
# a,b,c,d,e,f,h=0,1,2,3,4,5,6
# graph=[[a,b,3],[a,c,2],[b,d,5],
#        [d,e,7],[d,e,5],[e,f,6],
#        [d,f,8],[f,h,9],[h,a,1]]

# #define adjacency matrix
# def adjmatrix(v,g):
#     adj=[[0 for i in range(v)]for j in range(v)]
#     for i in range(len(g)):
#         adj[g[i][0]][g[i][1]]=[g[i][2]]
#         adj[g[i][1]][g[i][0]]=[g[i][2]] #undirected
#     return adj

# def prims(v,g):
#     adj=adjmatrix(v,g)
#     vertex=0 #sourcevertex
#     edges=[]
#     visited=[]
#     midedge=[None,None,float('inf')]

#     MST=[]
#     while(len(MST)!=v-1):
#         visited.append(vertex)
#         for ed in range(0,v):
#             if (adj[vertex][ed]!=0):
#                 edges.append([vertex,ed,adj[vertex][ed]])

#         for ed in range(len(edges)):
#             if(edges[ed][2] < midedge[2   ] and edges[ed][1] not in visited):
#                 midedge=edges[ed]
 
#         MST.append(midedge)
#         vertex=edges[1]
#         midedge=[None,None,float['inf']]

#     return MST
    
# print(prims(7,graph))
#define the graph
a,b,c,d,e,f,h=0,1,2,3,4,5,6
graph=[[a,b,3],[a,c,2],[b,d,5],
       [d,e,7],[d,e,5],[e,f,6],
       [d,f,8],[f,h,9],[h,a,1]]

#define adjacency matrix
def adjmatrix(v,g):
    adj=[[0 for i in range(v)]for j in range(v)]
    for i in range(len(g)):
        adj[g[i][0]][g[i][1]]=g[i][2]      # store weight, not list
        adj[g[i][1]][g[i][0]]=g[i][2]      # undirected
    return adj

def prims(v,g):
    adj=adjmatrix(v,g)
    vertex=0 #sourcevertex
    edges=[]
    visited=[]
    MST=[]

    while(len(MST)!=v-1):
        if vertex not in visited:
            visited.append(vertex)

        for ed in range(0,v):
            if (adj[vertex][ed]!=0 and ed not in visited):
                edges.append([vertex,ed,adj[vertex][ed]])

        midedge=[None,None,float('inf')]
        for ed in range(len(edges)):
            if(edges[ed][2] < midedge[2] and edges[ed][1] not in visited):
                midedge=edges[ed]
 
        MST.append(midedge)
        vertex=midedge[1]                   # move to next vertex

    return MST
    
print(prims(7,graph))
