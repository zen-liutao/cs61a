def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for b in branches(tree):
        if not is_tree(b):
            return False
    return True


def is_leaf(tree):
    return tree[1:] == []


def count_leaves(tree):
    if is_leaf(tree):
        return 1
    return sum([count_leaves(branch) for branch in branches(tree)])


def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    return sum([leaves(branch) for branch in branches(tree)], [])


def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t)+1)
    return tree(label(t), [increment_leaves(branch) for branch in branches(t)])


def increment(t):
    return tree(label(t)+1, [increment(branch) for branch in branches(t)])


def tree_max(t):
    """Return the maximum label in a tree.
    >>> t = tree(4, [tree(2, [tree(1)]), tree(10)])
    >>> tree_max(t)
    10
    """
    if is_leaf(t):
        return label(t)
    return max([tree_max(branch) for branch in branches(t)])


def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    return max([height(branch) + 1 for branch in branches(t)])


def square_tree(t):
    """Return a tree with the square of every element in t"""
    return tree(label(t)**2, [square_tree(branch) for branch in branches(t)])


def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if is_leaf(tree):
       if x == label(tree):
           return [label(tree)]
    for branch in branches(tree):
        path = [label(tree)] + find_path(branch,x)
        if x == label(branch):
            return path 
    return None



    
