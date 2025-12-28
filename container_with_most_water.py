def maxArea(heights):
        l = 0
        r = len(heights) - 1
        maxWater = 0
        while l < r:
            water = min(heights[l],heights[r]) * (r-l)
            maxWater = max(water,maxWater)

            if heights[l] >heights[r]:
                r-=1
            else:
                l+=1
        return maxWater
# testcase
height = [1,7,2,5,4,7,3,6]
print(maxArea(height))