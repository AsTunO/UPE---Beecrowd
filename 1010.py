line1 = input().split(" ")
line2 = input().split(" ")

cod1, qtd1, value1 = line1
cod2, qtd2, value2 = line2

print("VALOR A PAGAR: R$ {:.2f}".format(((int(qtd1) * float(value1)) + (int(qtd2) * float(value2)))))