# Alunos e usuários correspondentes no Github:
# Alexandre Marques Tortoza Canoa - Alexandre-Tortoza
# Arthur Capellazzi Fontana Amaral - arthurCpl
# Gabriel Berto Beckauser - BrielPastel
# Giuseppe Stringhini Adam - giuseppeadam

# Grupo: RA1 21

import sys
import os
from lexer import parseExpressao
from assembly import lerArquivo, gerarAssembly
from executarExpressão import executarExpressao

def exibirResultados(resultados):
    print("\nResultados das expressões:")
    for i, res in enumerate(resultados, 1):
        if isinstance(res, float):
            print(f"Linha {i}: {res:.1f}")
        else:
            print(f"Linha {i}: {res}")
    print("\n")

if __name__ == "__main__":

    if len(sys.argv) != 2:
            print("Erro: execute com um arquivo .txt")
            print("Exemplo: python script.py entrada.txt")
            sys.exit(1)

    arquivo = sys.argv[1]

    if not arquivo.endswith(".txt"):
        print("Erro: o arquivo deve ser .txt")
        sys.exit(1)

    if not os.path.isfile(arquivo):
        print(f"Erro: arquivo '{arquivo}' não encontrado")
        sys.exit(1)

    memoria, historico = {}, []
    todos_tokens = []
    resultados = []
    tokens_txt = ""

    linhas = lerArquivo(arquivo)
    i=0
    for linha in linhas:
        i += 1
        try:
            tokens = parseExpressao(linha)
            print(f"Tokens da linha {i}: {tokens}")
            tokens_txt += f"{tokens}\n"

            todos_tokens.extend(tokens)
            executarExpressao(tokens, memoria, historico)
            resultados.append(historico[-1])  
               
        except Exception as e:
            resultados.append(f"Erro: {e}")

    codigo_assembly = gerarAssembly(todos_tokens)
    nome_saida = arquivo.replace(".txt", ".s")
    with open(nome_saida, "w") as f:
        f.write(codigo_assembly)

    exibirResultados(resultados)

    caminho = arquivo.replace(".txt", "_tokens.txt")
    with open(caminho, "w") as f:
        f.write(tokens_txt)


    print(f"Assembly gerado em: {nome_saida}")
    print("Cole o conteúdo no CPulator: https://cpulator.01xz.net/?sys=arm")
    print("Selecione: ARMv7 DE1-SoC")

    