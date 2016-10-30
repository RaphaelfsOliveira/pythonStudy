print 'Welcome to the Pig Latin Translator!'

# variavel que faz parte do jogo
pyg = 'ay'

# entrada do usuário
original = raw_input("Enter a word: ")

# passando a palavra para letras minusculas
word = original.lower()

# take first letter
first = word[0]

# make word len() => retorna o tamanho de uma variavel
new_word = word[1:len(word)] + first + pyg

#  original.isalpha() => testa se em uma string só tem caracteres de texto
if len(original) > 0 and original.isalpha():
    
    print "Word OK: " + new_word
    
else:
    
    print "Word Error: " + original + " empty"
    




