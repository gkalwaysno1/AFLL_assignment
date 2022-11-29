import ply.yacc as yacc
import ply.lex as lex
#from lex_prg import tokens

tokens=['IF','ELSE','LCUR','S1','S2','RCUR','semicolon','LP','RP','ID','OP1','OP2','OP3','VAL','OP6']
t_IF=r'if'
t_ELSE=r'else'
t_LCUR=r'\{'
t_RCUR=r'\}'
t_S1='Statement_1'
t_S2='Statement_2'
t_LP=r'\('
t_RP=r'\)'
t_ID='a'
t_OP1=r'\!'
t_OP2=r'\='
t_OP3=r'\>'
t_OP6=r'\<'
t_VAL=r'[0-9][0-9]*'
#t_T=r'T'
#t_A=r'A'
t_semicolon=r'\;'

def t_error(t):
    print("Illegal character")
    t.lexer.skip(1)
def p_if(p):
    'S : IF LP C RP LCUR S1 semicolon RCUR ELSE LCUR S2 semicolon RCUR'
    print('\nCORRECT SYNTAX')

def p_C(p):
    '''C : ID OP1 OP2 VAL
        | ID OP2 OP2 VAL
        | ID OP3 OP2 VAL
        | ID OP6 OP2 VAL
        | ID OP3 VAL
        | ID OP6 VAL'''
    #p[0]=p[1]

def p_error(p):
    print("THE GIVEN INPUT HAS A SYNTAX ERROR \n")
lexer=lex.lex()
parser=yacc.yacc()

ip=input("Enter the if else syntax\n")#Sample format ->'if(a>=0){Statement_1;}else{Statement_2;}'
parser.parse(ip)