from enum import Enum

input_stream = ""

class TokenType(Enum):
    INVALID = -1
    EOF = 0
    LITERAL = 1
    L_PARENTHESE = 2
    R_PARETNHESE = 3
    ADD = 4
    SUB = 5
    MULT = 6
    DIV = 7
    MOD = 8

class Token:
    def __init__(self, type, val):
        self.type = type;
        self.val = val;
    def __str__(self):
        return str(self.val) + " : " + str(self.type)

def set_input(input):
    global input_stream
    input_stream = input

def next_token():
    global input_stream

    matched_token = TokenType.INVALID
    current_str = ""

    # Check for EOF before loop
    if (len(input_stream) == 0):
        matched_token = TokenType.EOF

    while (len(input_stream) > 0):
        
        # Skip whitespace
        if input_stream[0].isspace():
            input_stream = input_stream[1:]
            continue
        
        # Consume next char in input
        current_str += input_stream[0]

        # Test for matches

        if (match_literal(current_str)):
            matched_token = TokenType.LITERAL

        elif (current_str == '('):
            matched_token = TokenType.L_PARENTHESE

        elif (current_str == ')'):
            matched_token = TokenType.R_PARETNHESE

        elif (current_str == '+'):
            matched_token = TokenType.ADD

        elif (current_str == '-'):
            matched_token = TokenType.SUB

        elif (current_str == '*'):
            matched_token = TokenType.MULT

        elif (current_str == '/'):
            matched_token = TokenType.DIV

        elif (current_str == '%'):
            matched_token = TokenType.MOD
        
        else:
            if matched_token == TokenType.INVALID:
                break
            
            current_str = current_str[:len(current_str)-1]
            break

        input_stream = input_stream[1:]
    
    return Token(matched_token, current_str)

def match_literal(str): 
    if str.count('.') > 1:
        return False
    
    for char in str:
        if char not in "0123456789.":
            return False
    return True