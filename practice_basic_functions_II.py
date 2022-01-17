def countdown(num):
  listNum = []
  for x in range(num,-1,-1):
    listNum.append(x)
  return listNum

print(countdown(5))

def imprimir_y_devolver(listIn):
  print(listIn[0])
  return listIn[1]

print(imprimir_y_devolver([1,2]))

def primero_mas_longitud(listIn):
  return listIn[0] + len(listIn)

print(primero_mas_longitud([1,2,3,4,5]))

def valores_mayores_que_el_segundo(listIn):
  if len(listIn)<2:
    return False
  else:
    listOut = []
    for ele in listIn:
      if ele > listIn[1]:
        listOut.append(ele)
    return listOut

print(valores_mayores_que_el_segundo([5,2,3,2,1,4]))
print(valores_mayores_que_el_segundo([3]))


def length_and_value(size, val):
  list = []
  for x in range(size):
    list.append(val)
  return list

print(length_and_value(4,7))
print(length_and_value(6,2))