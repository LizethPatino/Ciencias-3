import ply.lex as lex

declaracion = (
    'DECLARACION_iniciar_programa',
    'DECLARACION_inicia_ejecucion',
    'DECLARACION_termina_ejecucion',
    'DECLARACION_finalizar_programa',
    'DECLARACION_nueva_instruccion',  
    )

expresion = (
    'EXPRESION_APAGATE',
    'EXPRESION_GIRAIZQ',
    'EXPRESION_AVANZA',
    'EXPRESION_COGEZUMBADOR',
    'EXPRESION_DEJAZUMBADOR',
    'EXPRESION_SALIRINSTRUCCION',
)
condicional = (
    'CONDICIONAL_SI',
    'CONDICIONAL_SINO',
    'CONDICIONAL_MIENTRAS',
    'CONDICIONAL_PARA',
    'CONDICIONAL_VACIA',
)
funcionBooleana = (
    'FUNCIONBOOL_frente-libre',
    'FUNCIONBOOL_frente-bloqueado',
    'FUNCIONBOOL_izquierda-libre',
    'FUNCIONBOOL_izquierda-bloqueada',
    'FUNCIONBOOL_derecha-libre',
    'FUNCIONBOOL_derecha-bloqueada',
    'FUNCIONBOOL_junto-a-zumbador',
    'FUNCIONBOOL_no-junto-a-zumbador',
    'FUNCIONBOOL_algun-zumbador-en-la mochila',
    'FUNCIONBOOL_ningun-zumbador-en-la mochila',   
    )
tokens = declaracion+expresion+condicional+( 'LETRA','DIGITO','COMENTARIO','PLUS','TIMES','DIVIDE','EQUALS')

t_ignore = ' \n'
t_COMENTARIO = r'{}'
t_EQUALS = r'='
t_LETRA = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_DIGITO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_DECLARACION_iniciar_programa(t):
    r'iniciar-programa'
    return t
def t_DECLARACION_inicia_ejecucion(t):
    r'inicia-ejecucion'
    return t
def t_DECLARACION_termina_ejecucion(t):
    r'termina-ejecucion'
    return t
def t_DECLARACION_finalizar_programa(t):
    r'finalizar-programa'
    return t
def t_DECLARACION_nueva_instruccion(t):
    r'define-nueva-instruccion'
    return t

def t_EXPRESION_APAGATE(t):
    r'apagate'
    return t
def t_EXPRESION_GIRAIZQ(t):
    r'gira-izquierda'
    return t
def t_EXPRESION_AVANZA(t):
    r'avanza'
    return t
def t_EXPRESION_COGEZUMBADOR(t):
    r'coge-zumbador'
    return t
def t_EXPRESION_DEJAZUMBADOR(t):
    r'deja-zumbador'
    return t
def t_EXPRESION_SALIRINSTRUCCION(t):
    r'sal-de-instruccion'
    return t



def t_CONDICIONAL_SINO(t):
    r'sino'
    return t
def t_CONDICIONAL_SI(t):
    r'si'
    return t
def CONDICIONAL_PARA(t):
    r'repetir'
    return t
def t_CONDICIONAL_MIENTRAS(t):
    r'mientras'
    return t





# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer
archivo = open("expresion.in", "r") 

for expresion in archivo.readlines():
    lex.input(expresion)
    print("\nExpresion : ")
    while True:
        tok = lex.token()
        if not tok: break
        print (str(tok.value) + " -> " + str(tok.type))

#######################################################


