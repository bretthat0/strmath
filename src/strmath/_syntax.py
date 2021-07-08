from strmath._lexer import *

class BranchNode:
    def __init__(self, name):
        self.name = name;
        self.subnodes = []
    def add(self, node):
        self.subnodes.append(node)

class LeafNode:
    def __init__(self, token):
        self.name = token.type.name;
        self.val = token.val;

def parse():
    
    tokens = []

    def next():
        tokens.append(next_token())
    
    def match(token_type):
        return tokens[-1].type == token_type

    # accepts token if valid
    def accept(token_type):
        if match(token_type):
            next()
            return True
        return False
    
    # throws error if token is not accepted
    def expect(token_type):
        if accept(token_type):
            return
        print("Syntax error! Token", token_type, "expected!")

    # literal | l_parenthese expression r_parenthese
    def factor():
        node = BranchNode("Factor")
        if match(TokenType.LITERAL):
            node.add(LeafNode(tokens[-1]))
            next()
        elif accept(TokenType.L_PARENTHESE):
            node.add(expression())
            expect(TokenType.R_PARETNHESE)
        else:
            # TODO: more concise error messages
            print("Syntax error!")
            next()
        return node

    # factor {(*/%) factor} 
    def term():
        node = BranchNode("Term")
        node.add(factor())
        while match(TokenType.MULT) or match(TokenType.DIV) or match(TokenType.MOD):
            node.add(LeafNode(tokens[-1]))
            next()
            node.add(factor())
        return node

    # [(+-)? term]
    def expression():
        node = BranchNode("Expression")
        if match(TokenType.ADD) or match(TokenType.SUB):
            node.add(LeafNode(tokens[-1]))
            next()
        node.add(term())
        while match(TokenType.ADD) or match(TokenType.SUB):
            node.add(LeafNode(tokens[-1]))
            next()
            node.add(term())
        return node
    
    # expression eof
    def statement():
        node = BranchNode("Statement")
        node.add(expression())
        expect(TokenType.EOF)
        return node
    
    next()

    root = BranchNode("Root")
    root.add(statement())

    return root