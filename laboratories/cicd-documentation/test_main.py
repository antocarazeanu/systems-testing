# test_tree.py
from tree import Tree

def setup_sample_tree():
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    return tree

def test__find_existing():
    tree = setup_sample_tree()
    assert tree._find(3, tree.root).data == 3
    assert tree._find(4, tree.root).data == 4
    assert tree._find(0, tree.root).data == 0
    assert tree._find(8, tree.root).data == 8
    assert tree._find(2, tree.root).data == 2

def test__find_nonexistent():
    tree = setup_sample_tree()
    assert tree._find(5, tree.root) is None
    assert tree._find(-1, tree.root) is None
    assert tree._find(10, tree.root) is None
    assert tree._find(7, tree.root) is None

if __name__ == "__main__":
    test__find_existing()
    test__find_nonexistent()
    print("All _find tests passed!")
