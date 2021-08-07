def remover_numero(lista):
  numero_a_remover = int(input("Ingresa el numero a remover: "))
  # Alternative: Count numbers, call remove X times
  for num in lista:
    if (num == numero_a_remover):
      lista.remove(num)