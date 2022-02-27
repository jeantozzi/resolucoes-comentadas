#Summation
#Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

#For example:
#summation(2) -> 3
#1 + 2

#summation(8) -> 36
#1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

def summation(num):
    return sum(range(1, num + 1))

    # Como não foi necessário retornar a lista com as etapas de cálculo, o problema
    # se resolve com a soma de um range().
    # Obs.: Como o limite superior do range é exclusivo, é necessário o +1.
    # range(1, 5) retorna uma lista [1, 2, 3, 4]
