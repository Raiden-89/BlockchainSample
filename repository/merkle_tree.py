from repository.hash_utils import simple_hash
import math
from graphviz import Digraph

class MerkleTree:
    def __init__(self, leaves: list[str], k: int):
        if k < 8:
            raise ValueError("Parametro k troppo basso: insicuro")
        self.k = k
        self.leaves = [simple_hash(leaf, k) for leaf in leaves]
        self.tree = self._build_tree(self.leaves)

    def _build_tree(self, nodes):
        if len(nodes) == 1:
            return nodes
        if len(nodes) % 2 == 1:
            nodes.append(nodes[-1])  # Duplica ultimo nodo se dispari
        parent = [simple_hash(nodes[i] + nodes[i+1], self.k) for i in range(0, len(nodes), 2)]
        return nodes + self._build_tree(parent)

    def get_root(self):
        return self.tree[-1]

    def validate(self):
        return self.get_root() == MerkleTree([leaf for leaf in self.leaves], self.k).get_root()

    def plot(self, filename="merkle_tree"):
        dot = Digraph()
        nodes = list(self.tree)
        idx = 0
        level = 0
        width = len(self.leaves)
        while width >= 1:
            for i in range(width):
                dot.node(f"{idx}", nodes[idx])
                if level > 0:
                    dot.edge(f"{(idx - width * 2) // 2}", f"{idx}")
                idx += 1
            level += 1
            width //= 2
        dot.render(filename, format="png", cleanup=True)
