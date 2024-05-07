""" def is_pangram(sentence):
    alphabets = set('abcdefghijklmnopqrstuvwxyz')
    sentence_letters = set(sentence.lower())
    return alphabets.issubset(sentence_letters)

sentence = "The quick brown fox jumps over the lazy dog"
print(is_pangram(sentence))
sentence = "You are an animal!"
print(is_pangram(sentence))
 """
def is_pangram(sentence):
    if set('abcdefghijklmnopqrstuvwxyz').issubset(sentence.lower()):
        return True
    else:
        return False
    
sentence = "The quick brown fox jumps over the lazy dog"
print(is_pangram(sentence))
sentence = "You are an animal!"
print(is_pangram(sentence))
