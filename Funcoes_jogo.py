#importações
import random

def transforma_base(questoes):
    base = {}
    for dicio in questoes:
        if dicio['nivel'] not in base.keys():
            base[dicio['nivel']] = []    
        base[dicio['nivel']].append(dicio)
    return base

def valida_questao(questao):
    correct = {}
    for chave in ['titulo', 'nivel', 'opcoes', 'correta']:
        if chave not in questao.keys():
            correct[chave] = 'nao_encontrado'

    if len(questao.keys()) != 4:
        correct['outro'] = 'numero_chaves_invalido'

    if 'titulo' in questao.keys() and len(questao['titulo'].strip()) == 0:
        correct['titulo'] = 'vazio'

    if 'nivel' in questao.keys():
        if questao['nivel'] not in ['facil','medio','dificil']:
            correct['nivel'] = 'valor_errado'
    
    if 'opcoes' in questao.keys():
        if len(questao['opcoes']) != 4:
            correct['opcoes'] = 'tamanho_invalido'
        else:
            for letra in ['A','B','C','D']:
                if letra not in questao['opcoes'].keys():
                    correct['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        if 'opcoes' not in correct.keys():            
            ops = {}
            for alt, resp in questao['opcoes'].items():
                if len(str(resp).strip()) == 0:
                    ops[alt] = 'vazia'
            if len(ops) > 0:
                correct['opcoes'] = ops
    if 'correta' in questao.keys():
        if questao['correta'] not in ['A','B','C','D']:
            correct['correta'] = 'valor_errado'

    return correct

def valida_questoes(lista_questao):
    lista_erros = []
    for q in lista_questao:
        valida = valida_questao(q)
        lista_erros.append(valida)
    return lista_erros

def sorteia_questao(base, nivel):
    sorteio = random.choice(base[nivel])
    return sorteio

def sorteia_questao_inedida(base, nivel, ja_sorteado):
    retorno = True
    while retorno:
        inedito = random.choice(base[nivel])
        if inedito not in ja_sorteado:
            ja_sorteado.append(inedito)
            retorno = False
    return inedito

def questao_para_texto(questao, numero_questao):
    texto = '----------------------------------------'
    texto += '\nQUESTÃO ' +str(numero_questao) + '\n\n'
    texto += questao['titulo'] + '\n'
    texto += '\nRESPOSTAS:\n'
    for alt, resp in questao['opcoes'].items():
        texto += alt + ': '+ resp + '\n'
    return texto

def gera_ajuda(questao):
    lista_pode = []
    for perg, alt in questao['opcoes'].items():
        if perg != questao['correta']:
            lista_pode.append(alt)
    
    num = random.randint(1,2)
    tip = random.sample(lista_pode, k=num)

    texto1 = 'DICA:\n'
    texto1 += 'Opções certamente erradas: ' +  ' | '.join(tip)

    return texto1