from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request,'diagnostico_educacional.html')




def inicio(request):
    return render(request, 'index.html')
    #return HttpResponse('ola mundo')

def ler_banco(nome):
    lista_nome=[
        {'nome':'Ana','idade':20},
        {'nome':'Pedro','idade':25},
        {'nome':'Joaquin','idade':27},
    ]
    for pessoa in lista_nome:
        if pessoa['nome'] == nome:
            return pessoa 
    else:
        return {'nome':'nome não encontrado', 'idade':0}


def metas(resquest, meta):
    return HttpResponse("a meta requerida foi:"+str(meta))


def fname(request, name):
    idade = ler_banco(name)['idade']
    return render(request, 'pessoa.html', {'v_idade':idade})