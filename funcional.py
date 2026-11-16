"""
Semanas 3 e 4 — Programação funcional

Regras do paradigma:
- sem `class` (exceto a namedtuple Item);
- sem laços `for`/`while` (compreensões são permitidas);
- nenhuma função altera a lista recebida.
"""

from collections import namedtuple
from functools import reduce

ALIQUOTA_PADRAO = 0.25

ALIQUOTAS = {"cesta_basica": 0.0, "reduzido": 0.10, "padrao": 0.25}

Item = namedtuple("Item", ["nome", "preco", "categoria", "quantidade"], defaults=[1])


def aliquota(categoria):
    """Alíquota da categoria; ValueError se ela não existir."""
    if categoria not in ALIQUOTAS:
        raise ValueError(f"Categoria inválida: {categoria!r}")
    return ALIQUOTAS[categoria]


def imposto_item(item):
    """Imposto do item: round(round(preco * aliquota, 2) * quantidade, 2)."""
    por_unidade = round(item.preco * aliquota(item.categoria), 2)
    return round(por_unidade * item.quantidade, 2)


def total_impostos(itens):
    """Soma dos impostos de todos os itens."""
    return round(sum(map(imposto_item, itens)), 2)


def total_compra(itens):
    """Soma de preço × quantidade (sem imposto) mais os impostos."""
    subtotal = sum(map(lambda item: item.preco * item.quantidade, itens))
    return round(subtotal + total_impostos(itens), 2)


def filtrar_por_categoria(itens, categoria):
    """Nova lista só com os itens da categoria informada."""
    return list(filter(lambda item: item.categoria == categoria, itens))


def ordenar_por_preco(itens, decrescente=False):
    """Nova lista ordenada pelo preço unitário."""
    return sorted(itens, key=lambda item: item.preco, reverse=decrescente)


def economia_total(itens):
    """Quanto se pagaria a mais se todos os itens tivessem a alíquota padrão."""
    com_padrao = sum(
        map(lambda item: round(item.preco * ALIQUOTA_PADRAO, 2) * item.quantidade, itens)
    )
    return round(com_padrao - total_impostos(itens), 2)


# ---------- Semana 4: funções de ordem superior ----------

def criar_calculadora(aliquota_padrao):
    """Devolve uma função calcular(item) que usa outra alíquota padrão (closure)."""
    if aliquota_padrao < 0:
        raise ValueError("A alíquota padrão não pode ser negativa.")

    aliquotas = {
        "cesta_basica": 0.0,
        "reduzido": aliquota_padrao * 0.4,
        "padrao": aliquota_padrao,
    }

    def calcular(item):
        por_unidade = round(item.preco * aliquotas[item.categoria], 2)
        return round(por_unidade * item.quantidade, 2)

    return calcular


def compor(*funcoes):
    """compor(f, g)(x) == f(g(x)): aplica as funções da direita para a esquerda."""
    return lambda x: reduce(lambda acumulado, f: f(acumulado), reversed(funcoes), x)


def valor_item(item):
    """Valor final do item (preço x quantidade + imposto)."""
    return round(item.preco * item.quantidade + imposto_item(item), 2)


def gerar_relatorio(itens):
    """Resumo da compra: valor por categoria, impostos, total e economia."""
    return {
        "por_categoria": {
            categoria: round(
                sum(map(valor_item, filtrar_por_categoria(itens, categoria))), 2
            )
            for categoria in ALIQUOTAS
        },
        "total_impostos": total_impostos(itens),
        "total": total_compra(itens),
        "economia": economia_total(itens),
    }
