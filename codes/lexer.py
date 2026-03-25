# -------------------------------------------------------
# Aluno 1: Analisador Léxico com Autômato Finito Determinístico
# -------------------------------------------------------
# Responsável: parseExpressao + estados do AFD + salvar_tokens
# -------------------------------------------------------


def estado_numero(linha, i):
    """
    Estado AFD: reconhece números reais no formato inteiro ou X.Y.
    Rejeita: começa com ponto (.5), termina com ponto (3.),
             dois pontos decimais (3.14.5).
    """
    numero = ""
    ponto = False

    while i < len(linha):
        c = linha[i]

        if c.isdigit():
            numero += c
        elif c == '.':
            if ponto:
                raise Exception(f"Número inválido: dois pontos decimais em '{numero}.'")
            if not numero:
                raise Exception("Número inválido: começa com ponto '.'")
            ponto = True
            numero += c
        else:
            break

        i += 1

    if numero.endswith('.'):
        raise Exception(f"Número inválido: termina com ponto '{numero}'")

    return numero, i


def estado_identificador(linha, i):
    """
    Estado AFD: reconhece identificadores formados apenas por letras maiúsculas.
    Rejeita qualquer identificador com letras minúsculas (ex.: 'mem', 'Res').
    Inclui a keyword RES e qualquer variável de memória (MEM, VAR, X, etc.).
    """
    ident = ""

    while i < len(linha):
        c = linha[i]

        if c.isalpha():
            ident += c
            i += 1
        else:
            break

    if not ident.isupper():
        raise Exception(f"Identificador inválido (deve ser totalmente maiúsculo): '{ident}'")

    return ident, i


def estado_operador(linha, i):
    """
    Estado AFD: reconhece operadores simples (+, -, *, /, %, ^)
    e o operador composto de divisão inteira (//).
    """
    c = linha[i]

    # caso especial: operador composto //
    if c == '/' and i + 1 < len(linha) and linha[i + 1] == '/':
        return "//", i + 2

    return c, i + 1


def estado_parentese(linha, i):
    """
    Estado AFD: reconhece parênteses de abertura '(' e fechamento ')'.
    """
    return linha[i], i + 1


def parseExpressao(linha):
    """
    Analisa uma linha de texto em notação RPN e retorna a lista de tokens.
    Implementa um AFD com cada estado como uma função separada.
    Valida balanceamento de parênteses.

    Tokens reconhecidos:
      - Números reais  : ex. 3, 3.14
      - Operadores     : +  -  *  /  //  %  ^
      - Identificadores: sequências de letras MAIÚSCULAS (inclui RES, MEM, VAR, etc.)
      - Parênteses     : ( )

    Retorna: lista de strings com os tokens da expressão.
    Lança Exception em caso de token inválido ou parênteses desbalanceados.
    """
    tokens = []
    i = 0
    profundidade = 0  # controla balanceamento de parênteses

    while i < len(linha):
        c = linha[i]

        # espaços são ignorados (separadores)
        if c.isspace():
            i += 1
            continue

        # dígito → estado_numero
        elif c.isdigit():
            token, i = estado_numero(linha, i)
            tokens.append(token)

        # letra → estado_identificador
        elif c.isalpha():
            token, i = estado_identificador(linha, i)
            tokens.append(token)

        # operadores aritméticos → estado_operador
        elif c in "+-*/%^":
            token, i = estado_operador(linha, i)
            tokens.append(token)

        # parêntese de abertura
        elif c == '(':
            token, i = estado_parentese(linha, i)
            tokens.append(token)
            profundidade += 1

        # parêntese de fechamento
        elif c == ')':
            if profundidade == 0:
                raise Exception(f"Parêntese ')' sem abertura correspondente na posição {i}")
            token, i = estado_parentese(linha, i)
            tokens.append(token)
            profundidade -= 1

        else:
            raise Exception(f"Token inválido: '{c}' na posição {i}")

    # após percorrer toda a linha, verifica se sobraram parênteses abertos
    if profundidade != 0:
        raise Exception(f"Expressão com {profundidade} parêntese(s) '(' sem fechamento")

    return tokens


def salvar_tokens(todos_tokens, caminho="tokens.txt"):
    """
    Salva os tokens de TODAS as linhas da última execução em um único arquivo,
    um token por linha, com cabeçalho e separador entre expressões distintas.

    Parâmetro:
        todos_tokens : lista de listas  [[tok, tok, ...], [tok, tok, ...], ...]
        caminho      : caminho do arquivo de saída (padrão: tokens.txt)
    """
    with open(caminho, "w") as f:
        for idx, tokens_linha in enumerate(todos_tokens):
            f.write(f"# expressao {idx + 1}\n")
            for token in tokens_linha:
                f.write(token + "\n")
            f.write("---\n")