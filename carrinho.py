from carrinho import calcular_total, aplicar_desconto

def test_calcular_total():
    resultado = calcular_total(10, 4)
    assert resultado == 30


def test_aplicar_desconto():
    total = 100
    desconto = 0.1
    resultado = aplicar_desconto(total, desconto)
    assert resultado == 90
