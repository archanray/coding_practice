from collections import Counter
def solution(r1, r2):
    cnt1, cnt2 = Counter(r1), Counter(r2)
    
    replacement = 0
    free_slots = 0
    for i in range(len(r1)):
        pair = r1[i] + r2[i]
        if pair == '??':
            free_slots += 1 
            continue
        if pair == 'WR' or pair == 'RW':
            continue
        if pair == 'WW' or pair == 'RR':
            return -1
        
        replacement += 1
        if r1[i] == 'W':
            cnt2['R'] += 1 
        elif r1[i] == 'R':
            cnt2['W'] += 1
        elif r2[i] == 'W':
            cnt1['R'] += 1
        elif r2[i] == 'R':
            cnt1['W'] += 1 
    # by this time, both rows should have the same total number of letters
    # So the diff between R and W should be the same for both rows
    diff1 = abs(cnt1['W'] - cnt1['R'])
    diff2 = abs(cnt2['W'] - cnt2['R'])
    print(f"{diff1} == ? {diff2}")
    if diff1 > free_slots:
        return -1
    
    replacement += diff1*2
    return replacement
    

# "?RW?WR", "?WR?RW"
# "W?WR?", "R??W?"
# "R?R??", "??W??"
print(solution("R?R??", "??W??"))
