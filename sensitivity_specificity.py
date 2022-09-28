def solution(A, B, q):

    # A = real state
    # B = test result
    # when q = False, return sensitivity = TP / (TP + FN)
    # when q = True, return specificity = TN / (FP + TN)
    
    if not q:
        
        tp = 0
        fn = 0
        
        i = 0
        while i < len(A):
            if B[i] == 0 and A[i] == 1:
                fn += 1
            elif B[i] == 1 and A[i] == 1:
                tp += 1
            
            i += 1
        
        return(float(tp / (tp + fn)))
        
    else:
        
        tn = 0
        fp = 0
        
        i = 0
        while i < len(A):
            if B[i] == 1 and A[i] == 0:
                fp += 1
            elif B[i] == 0 and A[i] == 0:
                tn += 1
            
            i += 1
        
        return(float(tn / (fp + tn)))
        

A = [1, 0, 1, 1, 0, 1]
B = [0, 1, 1, 0, 0, 1]
q = False
solution(A, B, q)
    
A = [1, 0, 1, 1, 0, 1]
B = [0, 1, 1, 0, 0, 1]
q = True
solution(A, B, q)


A = [1, 0, 0, 1, 0, 1, 1, 0]
B = [1, 1, 0, 1, 1, 1, 0, 1]
q = False
solution(A, B, q)

A = [1, 0, 0, 1, 0, 1, 1, 0]
B = [1, 1, 0, 1, 1, 1, 0, 1]
q = True
solution(A, B, q)





