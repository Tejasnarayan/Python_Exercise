def word_reverse(sentence):
    words = sentence.split(" ")#split sentence into list of words
    newwords = [word[::-1]for word in words]#reversing each words
    newsentence = " ".join(newwords)#joining the new list of words
    return newsentence

sentence = "Python is Awesome"
print(word_reverse(sentence))