from collections import deque

def solution(cacheSize, cities):
    time = 0
    
    if cacheSize == 0:
        time += (len(cities) * 5)
        return time
    
    cache = deque()
    
    for city in cities:
        if city.lower() in cache:
            time += 1
            cache.remove(city.lower())
            cache.append(city.lower())
        else:
            if len(cache) < cacheSize:
                cache.append(city.lower())
            else:
                cache.popleft()
                cache.append(city.lower())
            time += 5
    
    return time