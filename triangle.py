def generate(numRows):
    triangle = []
    if(numRows < 1): return triangle
    triangle.append([1])
    for idx in range(1, numRows):
        prev = triangle[idx-1]
        current = [1]
        triangle.append(current)
        for j in range(1, idx):
            current.append(prev[j-1] + prev[j])
        current.append(1)
    return triangle
    
print(generate(4))
