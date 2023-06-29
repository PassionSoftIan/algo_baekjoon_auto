def solution(citations):
    books = len(citations)
    citations.sort()
    
    for i in range(len(citations) - 1):
        if citations[i] >= books-i:
            return books-i
        
    return 0