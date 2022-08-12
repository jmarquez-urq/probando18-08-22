#!/usr/bin/python3

deuda = 1000
while deuda > 0:
    pago = int(input("Monto de la cuota: "))
    deuda = deuda - pago
    print("Resta pagar $", deuda)

print("Deuda saldada!")
if deuda < 0:
    print(f"Se pagaron ${-deuda} demás")
