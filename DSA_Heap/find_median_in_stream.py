'''
The median is the middle value in a sorted list of integers. 
For lists of even length, there is no middle value, 
so the median is the mean of the two middle values.

For example:

For arr = [1,2,3], the median is 2.
For arr = [1,2], the median is (1 + 2) / 2 = 1.5
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far.
Example 1:

Input:
["MedianFinder", "addNum", "1", "findMedian", "addNum", "3" "findMedian", "addNum", "2", "findMedian"]

Output:
[null, null, 1.0, null, 2.0, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.findMedian(); // return 1.0
medianFinder.addNum(3);    // arr = [1, 3]
medianFinder.findMedian(); // return 2.0
medianFinder.addNum(2);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
Constraints:

-100,000 <= num <= 100,000
findMedian will only be called after adding at least one integer to the data structure.

'''
import heapq
class MedianFinder:
    def __init__(self):
        self.minHeap,self.maxHeap = [],[]

    def addNums(self, num:int)->None:
        if not self.maxHeap or num<=self.maxHeap[0]:
            heapq.heappush(self.maxHeap,-num)
        else:
            heapq.heappush(self.minHeap,num)
        self.balanceHeaps()
    def balanceHeaps(self) -> None:
        if len(self.maxHeap)> len(self.minHeap)+1:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,val)
        elif len(self.minHeap)>len(self.maxHeap)+1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap,-val)
    def medianFinder(self)->float:
        if len(self.maxHeap)>len(self.minHeap):
            return -self.maxHeap[0]
        elif len(self.minHeap)>len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (-self.maxHeap[0]+self.minHeap[0])/2.0


if __name__=="__main__":
    mf = MedianFinder()
    input_arr = list(map(str,input().split(',')))
    res=[None]
    print(input_arr)
    i = 1
    while i<len(input_arr):
        if input_arr[i]=="addNum":
            
            i+=1
            mf.addNums(int(input_arr[i]))
            res.append(None)
        if input_arr[i]=="findMedian":
            res.append(mf.medianFinder())
        i+=1
    print(res)

    '''
    use test input : MedianFinder,addNum,1,findMedian,addNum,3,findMedian,addNum,2,findMedian
    '''
