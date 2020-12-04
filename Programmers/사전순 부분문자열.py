def solution(s):
    answer = ''
    word = []
    for letter in s:
        while len(word):
            if ord(word[-1]) < ord(letter) : 
                word.pop()
            else:
                break
        word.append(letter)
    answer = ''.join(word)
    return answer