'''

In the ancient kingdom of Numeria,
 scholars have discovered two ancient scrolls in the ruins of a long-lost library.
 These scrolls are believed to contain the secrets to unlocking a powerful artifact known as the "Crown of Wisdom." However, the scrolls are written in a numerical code that has baffled even the most learned scholars.

The scrolls contain two sequences of numbers, 
each representing a series of ancient spells. 
The scholars have determined that the key to deciphering the scrolls lies in 
finding the longest common prefix between pairs of numbers from the two sequences. A prefix of a number is formed by one or more of its digits, starting from its leftmost digit.

For example, the number 123 is a prefix of 12345, 
but 234 is not. Similarly, a common prefix of two numbers is a number that is a 
prefix of both. For instance, 5655359 and 56554 have a common prefix of 565, 
while 1223 and 43456 do not share any common prefix.

Your task is to help the scholars by writing a program that finds the 
length of the longest common prefix between all pairs of numbers (x, y) 
such that x belongs to the first sequence and y belongs to the second sequence. 
If no common prefix exists among any pairs, return 0.

 

Input Format
The first line contains an integer n, the number of elements in arr1.
The second line contains an integer m, the number of elements in arr2.
The next n lines contain the elements of arr1.
The following m lines contain the elements of arr2.
Constraints

1 <= arr1.length, arr2.length <= 5 * 104
1 <= arr1[i], arr2[i] <= 108

example:
Sample Input	Sample Output	Explanation
3
1
1
10
100
1000	3	There are 3 pairs (arr1[i], arr2[j]): - 
            The longest common prefix of (1, 1000) is 1. - 
            The longest common prefix of (10, 1000) is 10. - 
            The longest common prefix of (100, 1000) is 100. 
            The longest common prefix is 100 with a length of 3.
3
3
1
2
3
4
4
4	0	There exists no common prefix for any pair (arr1[i], arr2[j]), 
        hence we return 0. Note that common prefixes between 
        elements of the same array do not count.


'''

class TrieNode:
    def __init__(self):
        self.children = [None]*10
        self.isEndOfNumber = False
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    def addNumber(self,n:int)->None:
        curr = self.root
        num_seq = []
        while n>0:
            num_seq.append((n%10))
            n = n//10
        for c in num_seq[::-1]:
            if curr.children[c] == None:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOfNumber = True
    def prefixCount(self,n:int)->int:
        curr = self.root
        num_seq = []
        while n>0:
            num_seq.append((n%10))
            n = n//10
        prefix_count = 0
        for c in num_seq[::-1]:
            if curr.children[c]==None:
                return prefix_count
            curr = curr.children[c]
            prefix_count +=1
        return prefix_count


if __name__=="__main__":
    pt = PrefixTree()
    n_arr_count = int(input())
    m_arr_count = int(input())
    for i in range(n_arr_count):
        pt.addNumber(int(input()))
    maxCount = float("-inf")
    for i in range(m_arr_count):
        maxCount = max(maxCount,pt.prefixCount(int(input())))
    print(maxCount)
