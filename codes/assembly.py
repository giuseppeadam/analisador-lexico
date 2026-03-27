# Alunos e usuários correspondentes no Github:
# Alexandre Marques Tortoza Canoa - Alexandre-Tortoza
# Arthur Capellazzi Fontana Amaral - arthurCpl
# Gabriel Berto Beckauser - BrielPastel
# Giuseppe Stringhini Adam - giuseppeadam

# Grupo: RA1 21

#!/usr/bin/env python

_FUNCOES_AUXILIARES_ASM = """
push_d0:
    PUSH {R0, R1, R2, LR}
    LDR R0, =stack_data
    LDR R1, =stack_top
    LDR R2, [R1]
    LSL R2, R2, #3
    ADD R0, R0, R2
    VSTR D0, [R0]
    LDR R2, [R1]
    ADD R2, R2, #1
    STR R2, [R1]
    POP {R0, R1, R2, PC}

pop_d0:
    PUSH {R0, R1, R2, LR}
    LDR R1, =stack_top
    LDR R2, [R1]
    SUB R2, R2, #1
    STR R2, [R1]
    LDR R0, =stack_data
    LSL R2, R2, #3
    ADD R0, R0, R2
    VLDR D0, [R0]
    POP {R0, R1, R2, PC}
"""


def lerArquivo(nomeArquivo):
    linhas = []
    try:
        with open(nomeArquivo, "r") as file:
            for linha in file:
                linha = linha.strip()
                if linha:
                    linhas.append(linha)
    except Exception:
        print("Arquivo não encontrado")
        return []
    return linhas


def _eh_numero(token):
    try:
        float(token)
        return True
    except ValueError:
        return False


def _emitir_operacao_binaria(emit, instrucao):
    emit("    BL pop_d0")
    emit("    VMOV D1, D0")
    emit("    BL pop_d0")
    emit(f"    {instrucao} D0, D0, D1")
    emit("    BL push_d0")


def gerarAssembly(tokens):
    codigo = []
    constantes = []
    variaveis = {}
    proximo_id_constante = [0]
    proximo_id_potencia = [0]

    def emit(linha):
        codigo.append(linha)

    def nova_const(valor_str):
        label = f"const_{proximo_id_constante[0]}"
        proximo_id_constante[0] += 1
        constantes.append((label, valor_str))
        return label

    emit(".global _start")
    emit(".text")
    emit("_start:")

    for token in tokens:
        if token in ("(", ")"):
            continue

        elif _eh_numero(token):
            label = nova_const(token)
            emit(f"    LDR R0, ={label}")
            emit("    VLDR D0, [R0]")
            emit("    BL push_d0")

        elif token == "+":
            _emitir_operacao_binaria(emit, "VADD.F64")

        elif token == "-":
            _emitir_operacao_binaria(emit, "VSUB.F64")

        elif token == "*":
            _emitir_operacao_binaria(emit, "VMUL.F64")

        elif token == "/":
            _emitir_operacao_binaria(emit, "VDIV.F64")

        elif token == "//":
            emit("    BL pop_d0")
            emit("    VMOV D1, D0")
            emit("    BL pop_d0")
            emit("    VDIV.F64 D0, D0, D1")
            emit("    VCVT.S32.F64 S0, D0")
            emit("    VMOV R0, S0")
            emit("    VMOV S0, R0")
            emit("    VCVT.F64.S32 D0, S0")
            emit("    BL push_d0")

        elif token == "%":
            emit("    BL pop_d0")
            emit("    VMOV D1, D0")
            emit("    BL pop_d0")
            emit("    VCVT.S32.F64 S0, D0")
            emit("    VMOV R0, S0")
            emit("    VCVT.S32.F64 S1, D1")
            emit("    VMOV R1, S1")
            emit("    MOV R2, #0")
            emit("loop_div_0:")
            emit("    CMP R0, R1")
            emit("    BLT fim_div_0")
            emit("    SUB R0, R0, R1")
            emit("    ADD R2, R2, #1")
            emit("    B loop_div_0")
            emit("fim_div_0:")
            emit("    MUL R2, R2, R1")
            emit("    SUB R0, R0, R2")
            emit("    VMOV S0, R0")
            emit("    VCVT.F64.S32 D0, S0")
            emit("    BL push_d0")

        elif token == "^":
            numero_potencia = proximo_id_potencia[0]
            proximo_id_potencia[0] += 1
            emit("    BL pop_d0")
            emit("    VMOV D1, D0")
            emit("    BL pop_d0")
            emit("    VCVT.S32.F64 S2, D1")
            emit("    VMOV R3, S2")
            label_const_um = nova_const("1.0")
            emit(f"    LDR R0, ={label_const_um}")
            emit("    VLDR D2, [R0]")
            emit(f"loop_pot_{numero_potencia}:")
            emit("    CMP R3, #0")
            emit(f"    BLE fim_pot_{numero_potencia}")
            emit("    VMUL.F64 D2, D2, D0")
            emit("    SUB R3, R3, #1")
            emit(f"    B loop_pot_{numero_potencia}")
            emit(f"fim_pot_{numero_potencia}:")
            emit("    VMOV D0, D2")
            emit("    BL push_d0")

        elif token == "RES":
            emit("    BL pop_d0")
            emit("    VCVT.S32.F64 S0, D0")
            emit("    VMOV R0, S0")
            emit("    LDR R1, =history_count")
            emit("    LDR R1, [R1]")
            emit("    SUB R0, R1, R0")
            emit("    LDR R1, =results_history")
            emit("    LSL R0, R0, #3")
            emit("    ADD R1, R1, R0")
            emit("    VLDR D0, [R1]")
            emit("    BL push_d0")

        elif token.isupper() and token.isalpha():
            var_label = f"var_{token}"
            if token not in variaveis:
                variaveis[token] = var_label
                emit("    BL pop_d0")
                emit(f"    LDR R0, ={var_label}")
                emit("    VSTR D0, [R0]")
            else:
                emit(f"    LDR R0, ={var_label}")
                emit("    VLDR D0, [R0]")
                emit("    BL push_d0")

    emit("    B .")
    emit("")
    emit(_FUNCOES_AUXILIARES_ASM)
    emit(".data")
    for label, val in constantes:
        emit(f"{label}: .double {val}")
    for name, var_label in variaveis.items():
        emit(f"{var_label}: .double 0.0")
    emit("stack_top: .word 0")
    emit("stack_data: .space 256")
    emit("results_history: .space 256")
    emit("history_count: .word 0")

    return "\n".join(codigo)
