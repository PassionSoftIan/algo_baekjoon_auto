def solution(cap, n, deliveries, pickups):
    deliveries.reverse()
    pickups.reverse()
    answer = 0

    container = 0
    backup = 0

    for i in range(n):
        container += deliveries[i]
        backup += pickups[i]

        while container > 0 or backup > 0:
            container -= cap
            backup -= cap
            answer += (n - i) * 2
    return answer