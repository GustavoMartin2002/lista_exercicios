"""
4-A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. 
Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.
"""

valor = float(input("digite o valor: "))

print(f"""
valor do produto: {valor}
parcelas do produto:
2x sem juros: {valor/2}
3x sem juros: {valor/3}
4x sem juros: {valor/4}
5x sem juros: {valor/5}
""")