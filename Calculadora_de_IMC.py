print ("____________________________")
print ("   Calculadora de IMC            ")
print ("____________________________")
while True:
	try:
		altura = int (input ("Olá usuario, me diga, qual é sua altura em centimetros: "))
		break
	except ValueError:
		print ("Somente numeros inteiros")
while True:
	try:
		peso = float (input ("Agora me diga o seu peso: "))
		break
	except ValueError:
		print ("Somente numeros")
altura_m = altura / 100
imc = peso / altura_m ** 2
print (f"Seu Indice de massa corporal (IMC) é: {imc:.2f}")
if imc <18.5:
	print ("Você esta abaixo do peso")
elif imc <25:
	print ("Você esta no peso ideal")
elif imc <30:
	print ("Você esta sobrepeso")
elif imc <35:
	print ("Você esta obeso (Grau 1)")
elif imc <40:
	print ("Você esta obeso (Grau 2)")
else:
	print ("Você esta obeso mórbido (Grau 3) ")