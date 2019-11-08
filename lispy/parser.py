from lark import Lark, InlineTransformer
from pathlib import Path

from .runtime import Symbol


class LispTransformer(InlineTransformer):
    def start(self, *args): 
        return [Symbol.BEGIN, *args]

    def number(self,token):
        return float(token)

    def list(self,*args):
        return [Symbol.QUOTE, *args]

    def atom(self,value):
        if(str(value) == '#t') :
            return True
        elif(str(value) == '#f') :
            return False
        else :
            try :
                return int(value)
                except ValueError :
                    try :
                        return float(value)
                        except ValueError :
                            return Symbol(str(value))


def parse(src: str):
    """
    Compila string de entrada e retorna a S-expression equivalente.
    """
    return parser.parse(src)


def _make_grammar():
    """
    Retorna uma gramática do Lark inicializada.
    """

    path = Path(__file__).parent / 'grammar.lark'
    with open(path) as fd:
        grammar = Lark(fd, parser='lalr', transformer=LispTransformer())
    return grammar

parser = _make_grammar()