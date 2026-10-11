def lenghtofword(word_taken):

    if len(word_taken) >= 2:
    
        return word_taken[:2] + word_taken[-2:]

    return  "''"

print(lenghtofword('dropping'))
print(lenghtofword('on'))
print(lenghtofword('o'))
