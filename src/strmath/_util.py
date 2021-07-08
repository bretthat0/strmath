def print_tree(node, indents = 0):
    i = indents*4*' '
    print(i + node.name)
    if hasattr(node, "val"):
        print(i + "Value:", node.val)
    if hasattr(node, "subnodes"):
        print(i + "{")
        for n in node.subnodes:
            print_tree(n, indents + 1)
        print(i + "}")