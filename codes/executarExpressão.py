# Alunos e usuários correspondentes no Github:
# Alexandre Marques Tortoza Canoa - Alexandre-Tortoza
# Arthur Capellazzi Fontana Amaral - arthurCpl
# Gabriel Berto Beckauser - BrielPastel
# Giuseppe Stringhini Adam - giuseppeadam

# Grupo: RA1 21
# Aluno 2 - executarExpressao
import math
from lexer import parseExpressao

def executarExpressao(tokens, memoria, historico):
    """
    Parâmetros:
        tokens   : lista de strings gerada por parseExpressao
        memoria  : dict  { nome_variavel -> float }  — escopo do arquivo atual
        historico: list  [ float, ... ]              — resultados anteriores

    Lança Exception para:
        - pilha insuficiente (operandos faltando)
        - divisão por zero
        - acesso a RES com índice inválido
        - leitura de variável não inicializada
    """

    pilha = []
    i = 0

    while i < len(tokens):
        token = tokens[i]

        # Parênteses aninhados: 
        # ignora, pois a avaliação da pilha RPN lida com isso
        if token in ('(', ')'):
            pass

        # Verifica se é um número real
        # Se sim, transforma em Float
        elif ehNumero(token):
            pilha.append(float(token))

        # Operadores aritméticos
        elif token in ("+", "-", "*", "/", "//", "%", "^"):

            if len(pilha) < 2:
                raise Exception(f"Operador '{token}': operandos insuficientes na pilha")

            b = pilha.pop()
            a = pilha.pop()

            if token == "+":
                pilha.append(a + b)

            elif token == "-":
                pilha.append(a - b)

            elif token == "*":
                pilha.append(a * b)

            elif token == "/":
                if b == 0:
                    raise Exception("Divisão real por zero")
                pilha.append(a / b)

            elif token == "//":
                if b == 0:
                    raise Exception("Divisão inteira por zero")
                pilha.append(float(math.floor(a / b)))

            elif token == "%":
                if b == 0:
                    raise Exception("Resto de divisão por zero")
                pilha.append(float(math.fmod(a, b)))

            elif token == "^":
                pilha.append(a ** b)

        # Keyword RES: recupera resultado N linhas atrás
        elif token == "RES":
            # (N RES) -> usa N da pilha
            # (RES)   -> usa 1 como padrão (último resultado)
            if pilha and pilha[-1] == int(pilha[-1]):
                n = int(pilha.pop())
            else:
                n = 1

            if n <= 0 or n > len(historico):
                raise Exception(
                    f"RES: índice {n} fora do intervalo "
                    f"(histórico tem {len(historico)} entradas)"
                )
            pilha.append(historico[-n])

        # MEM implementa atribuição:
        # padrão (V MEM NOME) -> armazena o valor V na variável NOME
        elif token == "MEM":
            i += 1
            if i >= len(tokens):
                raise Exception("MEM: esperado nome de variável após MEM")

            nome = tokens[i]

            if not nome.isalpha() or not nome.isupper():
                raise Exception(f"MEM: nome de variável inválido '{nome}'")

            if not pilha:
                raise Exception("MEM: pilha vazia ao tentar salvar variável")

            memoria[nome] = pilha[-1]   # salva

        # identificador de variável -> LEITURA
        # (NOME) -> empilha o valor armazenado em NOME com certas condições 
        elif token.isalpha() and token.isupper():
            if token not in memoria:
                raise Exception(f"Variável '{token}' não foi inicializada")
            pilha.append(memoria[token])

        else:
            raise Exception(f"Token desconhecido: '{token}'")

        i += 1

    if not pilha:
        raise Exception("Expressão vazia: nenhum resultado na pilha")

    resultado = pilha[-1]
    historico.append(resultado)

    return resultado

# Função auxiliar: valida se token é número 
def ehNumero(token):
    try:
        float(token)
        return True
    except ValueError:
        return False


def testar(linha, memoria, historico):
    try:
        tokens = parseExpressao(linha)
        resultado = executarExpressao(tokens, memoria, historico)
        print(f"[OK]   {linha} → {resultado}")
    except Exception as e:
        print(f"[ERRO] {linha} → {e}")


def testarExpressoes():
    memoria, historico = {}, []

    print("=== TESTES VÁLIDOS ===")
    testar("(3.14 2.0 +)",          memoria, historico)
    testar("(1 RES)",               memoria, historico)
    testar("(3.14 MEM X)",          memoria, historico)
    testar("(X)",                   memoria, historico)
    testar("(3 RES)",                   memoria, historico)

    print("\n=== TESTES INVÁLIDOS ===")
    testar("(3.14.5 2.0 +)",        memoria, historico)
    testar("(0 0 /)",               memoria, historico)
    testar("(MEM Z)",               memoria, historico)

if __name__ == "__main__":
    testarExpressoes()