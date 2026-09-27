def solution(word):
    dictOfChars = {}
    count = 1
    n = len(word)
    for i in range(n):
        if dictOfChars.get(word[i], 0) == 0:
            dictOfChars[word[i]] = i+1
        else:
            count += 1
            dictOfChars = {}
            dictOfChars[word[i]] = i+1
    return count

inputs = "paracycle"
print(solution(inputs))