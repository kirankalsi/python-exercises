def best_conjugation(string):
    text_file = 'wordlist.txt'
    f_contents = open(text_file, 'r')
    subwords = []
    total = len(subwords)
    words_list = [word for line in f_contents for word in line.split()]
    for word in words_list:
        if word in string:
            subwords.append(word)
    return subwords 

print(best_conjugation('awesomeness'))







#WIP code to only produce subwords without repeat letters
'''
def best_conjugation(string):
    text_file = 'wordlist.txt'
    f_contents = open(text_file, 'r')
    subwords = []
    words_list = [word for line in f_contents for word in line.split()]
    for word in words_list:
        [subwords.append(word) for word in words_list if word not in subwords]
    return subwords 

print(best_conjugation('apple'))
'''
    