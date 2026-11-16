"""
Semana 3 — Reescrevendo com programação funcional

Regras do paradigma:
- sem `class` (exceto a namedtuple Item);
- sem laços `for`/`while` (compreensões são permitidas);
- nenhuma função altera a lista recebida.
"""

from collections import namedtuple

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
