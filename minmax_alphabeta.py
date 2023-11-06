class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def is_terminal(self):
        return not bool(self.children)

    def evaluate(self):
        return self.value

    def get_children(self):
        return self.children


def minimax(node, depth, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate()

    if maximizing_player:
        max_eval = float('-inf')
        for child in node.get_children():
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.get_children():
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval


def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate()

    if maximizing_player:
        max_eval = float('-inf')
        for child in node.get_children():
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.get_children():
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


# Example Usage:
if __name__ == "__main__":
    # Create a simple tree for testing
    root = Node(0)
    child1 = Node(3)
    child2 = Node(5)
    child3 = Node(2)
    child4 = Node(9)

    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(child3)
    child1.add_child(child4)

    # Test Minimax
    print("Minimax Result:", minimax(root, 3, True))

    # Test Alpha-Beta Pruning
    print("Alpha-Beta Pruning Result:", alpha_beta(root, 3, float('-inf'), float('inf'), True))
