print('welcome to waldos')
vende=input('put your name:')
print(vende, 'welcome') 

arroz=input('first article:')
precio1=int(input('price: '))

coca=input('second article: ')
precio2=int(input('price: '))

jam=input('thirdarticle: ')
precio3=int(input('price: '))

uve=input('fortharticle: ')
precio4=int(input('price: '))

toast=input('five article: ')
precio5=int(input('price: '))

print('***************ticket****************')
print('you bougth',arroz,'for', precio1, 'monkey money')
print('you bougth',coca, 'for', precio2, 'monkey money')
print('you bougth', jam,'for', precio3, 'monkey money')
print('you bougth',uve,'for', precio4, 'monkey money')
print('you bougth',toast,'for', precio5, 'monkey money')
print('the total is:',(precio1+precio2+precio3+precio4+precio5))
print('iva is:',(precio1*precio2*precio3*precio4*precio5*1.16))
