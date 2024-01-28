from distutils.command.build import build
import heapq
def ksmallest(ksmall, ArrNum):
    pqueue = []
    if (ksmall > len(ArrNum)):
        ArrNum.sort()
        return ArrNum
    for i in range(ksmall):
        heapq.heappush(pqueue, -1*ArrNum[i])
    for i in range(ksmall, len(ArrNum)):
        if (-1*ArrNum[i] > pqueue[0]):
            heapq.heapreplace(pqueue, -1*ArrNum[i]) 
    temp_arr = [element * -1 for element in pqueue]
    
    temp_arr.sort()
    return temp_arr

if __name__ == "__main__":
    ArrNum = range(1000000,0,-1)
    print( ksmallest(3, ArrNum))

