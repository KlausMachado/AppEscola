import re
def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email)
    
def validar_nota(entrada):
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            return nota
        else:
            print("A nota deve ser um inteiro entre 0 e 10.")
    except ValueError:
        print("Nota invalida.")        
    return None

def media_notas(notas_str):
    notas = list(map(float, notas_str.split(",")))
    media = sum(notas) / len(notas)
    return media
