#!/usr/bin/env python3

import os
from lexer import parseExpressao
from assembly import lerArquivo, gerarAssembly


def test_ler_arquivo_valido():
    nome_arquivo = "./tmp-file.txt"

    with open(nome_arquivo, "w") as file:
        file.write("linha 01\nlinha 02\nlinha 03")

    resultado = lerArquivo(nome_arquivo)
    esperado = ["linha 01", "linha 02", "linha 03"]
    assert resultado == esperado

    os.remove(nome_arquivo)


def test_ler_arquivo_invalido():
    resultado = lerArquivo("arquivo_que_nao_existe.txt")
    assert resultado == [], f"Esperado [], obtido {resultado}"


def test_assembly_adicao():
    tokens = parseExpressao("(3.0 2.0 +)")
    asm = gerarAssembly(tokens)

    assert ".global _start" in asm
    assert "VADD.F64" in asm
    assert "const_0: .double 3.0" in asm
    assert "const_1: .double 2.0" in asm
    assert "stack_data" in asm


def test_assembly_aninhado():
    tokens = parseExpressao("((2.0 3.0 *) (4.0 5.0 *) /)")
    asm = gerarAssembly(tokens)

    assert "VMUL.F64" in asm
    assert "VDIV.F64" in asm


def test_assembly_divisao_inteira():
    tokens = parseExpressao("(7.0 2.0 //)")
    asm = gerarAssembly(tokens)

    assert "SDIV" in asm
    assert "VCVT.S32.F64" in asm
    assert "VCVT.F64.S32" in asm


def test_assembly_potencia():
    tokens = parseExpressao("(2.0 3.0 ^)")
    asm = gerarAssembly(tokens)

    assert "loop_pot" in asm
    assert "VMUL.F64" in asm


def test_assembly_memoria():
    tokens1 = parseExpressao("(5.0 TOTAL)")
    tokens2 = parseExpressao("(TOTAL)")
    asm1 = gerarAssembly(tokens1)
    asm2 = gerarAssembly(tokens2)

    assert "VSTR" in asm1
    assert "var_TOTAL" in asm1
    assert "VLDR" in asm2
