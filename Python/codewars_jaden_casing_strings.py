#Jaden Casing Strings
#Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.
#
#Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.
#
#Example:
#
#Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
#Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def to_jaden_case(string):
    return " ".join([word.capitalize() for word in string.split()])

    # Foi utilizado list comprehension para gerar uma lista, e o " ".join() para
    # juntar os elementos desta lista separando-os por espaço.
    # O simples str.title() não resolve o problema, visto que ele transforma em
    # caixa alta qualquer caracter depois de um não-alfabético. Isto significa que
    # "Aren't" viraria "Aren'T", o que não queremos.
    # Assim, foi preciso tratar cada palavra como uma string, e utilizar o
    # str.capitalize(), que modifica somente o primeiro caracter da string (sendo ele alfabético ou não).
