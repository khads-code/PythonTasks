def word(word_taken):  
  length = len(word_taken)  
  
  if length > 2:  
    if word_taken[-3:] == 'ing':  
      word_taken += 'ly'  
    else:  
      word_taken += 'ing'  
  
  return word_taken  
print(word('abc'))  
print(word('string'))  
print(word('on')) 
