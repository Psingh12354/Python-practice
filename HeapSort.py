import heapq as hq
def heapsort(i):
    li=[]
    for value in i:
        hq.heappush(li,value)
    return [hq.heappop(li) for i in range(len(li))]
print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
