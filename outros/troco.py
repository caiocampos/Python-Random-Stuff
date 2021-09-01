moedas = [100, 50, 20, 10, 5, 2, 1,
          float(0.5), float(0.25), float(0.1),  float(0.05)]
print("Digite o valor da compra:")
preco = float(input("   "))
print("Digite a quantia de dinheiro entregue:")
dinheiro = float(input("   "))
troco = dinheiro - preco
print

if troco > 0:
    print("Valor do troco: R$ %s." %troco)
    print
    for p in moedas:
        if troco >= p:
            n = int(troco / p)
            r = troco - p * n
            print(': %s nota(s) de R$ %s.' %(n, p))
            troco = r

else:
    print('O dinheiro entregue é menor do que o valor da compra.')
