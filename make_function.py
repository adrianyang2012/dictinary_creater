def make_dic(words, descption):    #make a function 
  dictianary = {}                  #create a list
  for i in range(0,len(words)):    # go threw the word list
    dictianary[words[i]] = descption[i]  # add to dictinary
  return dictianary               #return the dictinary
