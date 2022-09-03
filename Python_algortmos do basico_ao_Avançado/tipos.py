import types


def diz_tipo(a):
    if isinstance(a,str):
        return 'String'
    elif isinstance(a,list):
        return 'Lista'
    elif isinstance(a,dict):
        return 'Dict'
    elif isinstance(a,float):
        return 'Numero Decimal'
    elif isinstance(a,int):
        return 'Numero Inteiro'
    elif isinstance(a, types.FunctionType):
        return 'Função'
    elif isinstance(a, types.BuiltinFunctionType):
        return 'Função Interna'
    else:
        return str(type(a))

print(diz_tipo(10))
print(diz_tipo(10.5))
print(diz_tipo('Alguém'))
print(diz_tipo([1,2,3]))
print(diz_tipo({'a':1, 'b': 50}))
print(diz_tipo(print()))
print(diz_tipo(None))