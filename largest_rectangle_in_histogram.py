def largestRectangleArea(heights):
    maxArea = 0
    for index,height in enumerate(heights):
        stack = []

        # checar lado derecho
        for i in range(index, len(heights)):
            if heights[i] >= height:
                stack.append(heights[i])
                continue
            break
        # checar lado izquierdo
        for i in range(index - 1, -1, -1):
            if heights[i] >= height:
                stack.append(heights[i])
                continue
            break
        # calcular area
        maxArea = max(maxArea,height * len(stack))

    return maxArea

# testcase
heights = [7,1,7,2,2,4]
print(largestRectangleArea(heights))