

def solution(S):
    
    sol = True
    
    if len(S) == 0:
        return(True)
    
    previous_elem = S[0]
    i = 1
    
    while i < len(S):
        current_elem = S[i]
        if previous_elem == "b" and current_elem == "a":
            return(False)
        previous_elem = current_elem
        i += 1
        
    return(sol)



S = "aabbb"
solution(S)
S = "ba"
solution(S)
S = "aaa"
solution(S)
S = "b"
solution(S)
S = "abba"
solution(S)
S = ""
solution(S)

