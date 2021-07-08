from strmath._lexer import *
from strmath._syntax import *
#import strmath._util

def evaluate(input):
    set_input(input)
    ast = parse()

    def is_leaf(node):
        return hasattr(node, "val")

    def factor(node):
        subnode = node.subnodes[0]
        if (is_leaf(subnode)):
            return float(subnode.val)
        else:
            return expression(subnode)

    def term(node):
        val = factor(node.subnodes[0])

        for x in range(1, len(node.subnodes), 2):
            if is_leaf(node.subnodes[x]):
                if node.subnodes[x].name == "MULT":
                    val *= factor(node.subnodes[x+1])
                elif node.subnodes[x].name == "DIV":
                    val /= factor(node.subnodes[x+1])
                elif node.subnodes[x].name == "MOD":
                    val %= factor(node.subnodes[x+1])
        
        return val

    def expression(node, depth = 0):
        if node.subnodes[depth].name == "Term":
            depth -= 1
        
        prefix = term(node.subnodes[depth + 1])
        if node.subnodes[depth].name == "SUB":
            prefix *= -1
        
        suffix = 0
        if (len(node.subnodes) - depth > 2):
            suffix = expression(node, depth + 2)

        return prefix + suffix


    def statement(node):
        return expression(node.subnodes[0])
    
    return statement(ast.subnodes[0])