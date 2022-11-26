#!/usr/bin/env python3

import matplotlib
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram

# Exercícios de computação clássica

def exercicio_01(n):
    return f'{n:04b}'

def exercicio_02(*args):
    if len(args) > 0:
        a =args[0]
    else:
        a = "Levando em conta que cada bit contém 2 estados de informação, 2^n"
    pergunta = "Se você tem um número N de bits, em quantos estados diferentes podemos representa-los?"
    print(pergunta)
    print(f"Resposta: {a}")


class primeiro_circuito():
    qc_out = QuantumCircuit(8)
    qc_out.measure_all()

    def simular_circuito(qc):
        simulador = Aer.get_backend('aer_simulator') # Backend da simulação, caso eu estivesse utilizando um computador quântico, apenas mudaria este backend para lhe entregar instruções
        resultado = simulador.run(qc).result()
        counter = resultado.get_counts()
        return counter

    def plotar_histograma(hist):
        plot_histogram(simular_circuito(qc_out))
