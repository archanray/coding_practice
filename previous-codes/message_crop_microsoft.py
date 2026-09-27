# this should be easy
def solution(message, k):
    words = message.split(" ")
    length = 0
    output = ""
    for word in words:
        if length + 1 + len(word) > k:
            if length == 0:
                return "..."
            else:
                return output+" ..."
        else:
            output = output + " " + word
            length += len(word) + 1
    return output

K = 20
string = "how are you"
print(solution(string, K)+"EOL")