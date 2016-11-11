def censor(text,word):
    tx = text.split()

    for i in range(0,len(tx)):
        if tx[i] == word:
            tx[i] = "*" * len(tx[i])

    return tx


print censor("this hack is wack hack", "hack")
