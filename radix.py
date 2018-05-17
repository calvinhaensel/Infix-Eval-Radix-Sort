def radixsort(unsortedlst, size):
    maxLen = maxString(unsortedlst)
    o0 = ord(chr(1)) - 1;
    oz = ord('z') - 1;
    n = oz - o0 + 2; 
    buckets = [[] for i in range(0, n)] 
    for position in reversed(range(0, maxLen)):
        for string in unsortedlst:
            index = 0 
            if position < len(string): 
                index = ord(string[position]) - o0
            buckets[index].append(string)
        del unsortedlst[:]
        for bucket in buckets: 
            unsortedlst.extend(bucket)
            del bucket[:]
    return unsortedlst

def maxString(unsortedlst):
    maxLen = -1
    for string in unsortedlst:
        strLen = len(string)
        if strLen > maxLen:
            maxLen = strLen
    return maxLen

def main():
    prlist = ['This', 'is', 'a', '/est', 'string', 'from', 'Andrew']
    srtlst = radixsort(prlist, len(prlist))
    print(srtlst)
    prlist.sort()
    print(prlist)
if __name__=='__main__':
    main()