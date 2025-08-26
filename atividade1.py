import os
os.system('cls // clear')


compras_do_mes = int(input('Quantas compras o cliente fez este mês? '))
valor_compra = float(input('Qual o valor da compra atual R$ '))

valor_final = valor_compra


if compras_do_mes >= 3 and valor_compra > 500:
    valor_final *= 0.83  
elif compras_do_mes > 3:   
    valor_final *= 0.93
elif valor_compra > 500:  
    valor_final *= 0.90

print("\n=== RESUMO DA COMPRA ===")
print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Valor final:    R$ {valor_final:.2f}")

