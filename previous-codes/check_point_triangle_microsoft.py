def area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)

def solution(inputs):
    x1, y1, x2, y2, x3, y3, x, y = inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5], inputs[6], inputs[7]
    AreaABC = area(x1, y1, x2, y2, x3, y3)
    AreaAPB = area(x1, y1, x2, y2, x, y)
    AreaAPC = area(x1, y1, x3, y3, x, y)
    AreaBPC = area(x2, y2, x3, y3, x, y)
    
    if AreaAPB+AreaAPC+AreaBPC == AreaABC:
        return True
    return False

A = (0, 0)
B = (10, 30)
C = (20, 0)
P = (30, 15)
inputs = [A[0], A[1], B[0], B[1], C[0], C[1], P[0], P[1]]
print(solution(inputs))