
def missing_integer(A):
    import numpy as np
    s = set(A)
    l = np.array(list(s))
    l = [item for item in l if item > 0]
    l = sorted(l, reverse = True)
    current_sol = 1
    
    if len(l) > 0:
        current_elem = l.pop()
        while current_sol >= current_elem and l:
            current_elem = l.pop()
            current_sol += 1
            
        if not l and current_sol >= current_elem:
            current_sol += 1
    
    return(current_sol)

A = [2, 4, 2, 6]
missing_integer(A)
A = [1, 3, 6, 4, 1, 2]
missing_integer(A)
A = [1, 2, 3]
missing_integer(A)
A = [-1, -3]
missing_integer(A)
