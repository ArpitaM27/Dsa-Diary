class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0

        for i in range(len(flowerbed)):

            
            if i == 0:
                if flowerbed[i] == 0 and (len(flowerbed) == 1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    count += 1
                continue

        
            if i == len(flowerbed)-1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    count += 1
                continue

            
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count += 1

        return count>=n
        