#FindPairs
def find_pairs(nums,target):
    for i in range(len(num)):
      for j in range(i+1,len(nums)):
          if num[i]+num[j]==target:
        print(i,j)
find_pairs([1,2,3,4],5)
