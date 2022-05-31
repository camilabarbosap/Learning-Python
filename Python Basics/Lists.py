#Lists

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2.5, 'a', True]

#List slicing
string = 'helloooo'
string[0:2:1]

#Data Structure

amazon_cart = [
  'notebooks', 
  'sunglasses',
  'toys', 
  'grapes'
]

amazon_cart[0] = 'laptop' #altera na lista
new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(amazon_cart[1:3])
print(new_cart)
print(amazon_cart)


#List Methods

basket = [1, 2, 3, 4, 5]

#adding
new_list = basket.append(100)
print(basket)
print(new_list) #neste caso não funciona porque o append não serve pra criar uma nova variável, apenas para mudar a que está associada

new_list = basket
print(new_list)

#insert serve para inserir em uma determinada posição. além disso, apresenta a mesma característica do append (não retorna valor)

new_list.insert(2, 98)
print(new_list)

#extend
new_list.extend([100])
print(new_list)

#removing (remove o ultimo iten da lista/ não retorna valor)
basket.pop()
basket.pop(0)
print(basket)


basket.remove(4)
print(basket)

#remove tudo da lista 
basket.clear()
print(basket)
