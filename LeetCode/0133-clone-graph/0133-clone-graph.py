"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node):
            if node and node.val not in visited:
                newNode = Node(node.val, [])
                visited[newNode.val] = newNode
                newNode.neighbors = [
                    visited.get(n.val) or dfs(n) for n in node.neighbors
                ]
                return newNode

        return dfs(node)