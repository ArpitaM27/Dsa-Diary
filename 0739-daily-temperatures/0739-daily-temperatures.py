
class Solution(object):
    def dailyTemperatures(self, temperatures):
      arr=[0]*len(temperatures)
      stack=[]
      i=0
      for i in range(len(temperatures)):
          while stack and temperatures[i]>temperatures[stack[-1]]:
              distance=i-(stack[-1])
              arr[stack.pop()]=distance
          stack.append(i)
      return arr