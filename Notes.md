# Binary search tree
- Each node contains at most 2 children (0,1,2)
- Left subtree of a node will have values less than the node*.
- Right subtree of a node will have values greater than the node*.
- Inorder traversal always returns the elements sorted in ascending order.
- No duplicate nodes
- You can contruct BST when given Postorder and Preorder traversals. You just have to create an inorder traversal (arrange the nodes in ascending order)


# AVL Tree
- It is a BST.
- Height of left subtree - Height of right subtree = (-1, 0, 1)
- The difference is know as the **Balance Factor**
- Duplicate elements are not allowed.

# Graphs
- Best ways to represent it
    - Adjacency matrix - best when the graph is a **dense graph** (Nodes are connected to many other nodes in the graph)
        - Has a space complexity of O(n ^ 2) since it is an n*n matrix
    - Adjacency list - best for a **sparse graph**
        - Has a space complexity of O(n + 2e). The **2e** is because a vertex is repeated for two nodes. *1->2* and *2->1*
## Graphs (Traversal techniques)
### BFS (Level Order)
- Queue is used.
- Visit all the adjacent nodes first.
### DFS
- Stack is used.
- Difference with BFS is you visit only one of the adjacent nodes instead of all the adjacent nodes.

## Spanning tree
 - Same number of vertices
 - Edges  = Vertices - 1
 - A subgraph of a graph
 - Graph must be connected.

 ### Minimum (Cost) Spanning tree
 #### Prim's Algorithm
  - Start with the edge with the smallest cost and keep going (connected smallest) till of the vertices have been visited.
  - Make sure you remove loops and parallel edges

 #### Kruskal's Algorithm
 - Select the minimum cost edge but do not include it if it forms a cycle.
 - Time complexity is O(n^2)
 - Possible to find MST for a disconnected graph but only gives spanning tree for those individual compnonents and not the entire graph.

 - Cost should always be optimum (minimum) even if the spanning tree changes.
 - m vertices and m-1 edges

 ## Dijkstra Algorithm
 - Single source shortest path problem
 - if(d(u) + c(u,v) < d(v))
        d(v) = d(u) + c(u,v)
 - The formula is called **Relaxation**

 - A bit complex to work with negative cost of edges. (May or may not work)
 - Relaxation only done once

 ## Bellman Ford Algorithm
 - Single source shortest path problem
 - Works even with edges that have negative weight/cost
 - Slower than Dijkstra
 - When n is the number of vertices, you have to relax all the edges, n-1 times
 - Uses the same relaxation technique
 - Time complexity is O(n^3)
 - Will not give the correct answer when the sum of a cycle is a negative value



 # Algorithm concepts
 ## Recurrence relation
 - Time complexity is O(n)
 - Where T is time T(n) = T(n-1) + 1