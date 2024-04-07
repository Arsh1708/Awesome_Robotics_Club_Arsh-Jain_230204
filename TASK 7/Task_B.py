import cv2
import numpy as np
import matplotlib.pyplot as plt

def shortestPath(grid, k):
    m, n = len(grid), len(grid[0])
    DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[[False] * (k + 1) for _ in range(n)] for _ in range(m)]
    queue = deque([(0, 0, k, [(0, 0)])])  # Include the path in the queue
    steps = 0
    
    while queue:
        size = len(queue)
        
        while size > 0:
            curr_x, curr_y, obs, path = queue.popleft()
            if curr_x == m - 1 and curr_y == n - 1:
                # Filter out positions with value 1 from the final path
                final_path = [(x, y) for x, y in path if grid[x][y] == 0]
                return steps, final_path  # Return steps and filtered path if destination reached
            
            for dx, dy in DIR:
                next_x, next_y = curr_x + dx, curr_y + dy
                next_obs = obs
                
                if 0 <= next_x < m and 0 <= next_y < n:
                    if grid[next_x][next_y] == 0 and not visited[next_x][next_y][next_obs]:
                        queue.append((next_x, next_y, next_obs, path + [(next_x, next_y)]))
                        visited[next_x][next_y][next_obs] = True
                    elif grid[next_x][next_y] == 1 and next_obs > 0 and not visited[next_x][next_y][next_obs - 1]:
                        queue.append((next_x, next_y, next_obs - 1, path + [(next_x, next_y)]))
                        visited[next_x][next_y][next_obs - 1] = True
            
            size -= 1
        steps += 1
    
    return -1, []  # Return -1 and empty path if destination is unreachable


# Load the image
image = cv2.imread('img2.jpg')

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load the image.")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply bilateral filter to keep edges sharp and blur low frequency regions. It reduces noise.
blurred = cv2.bilateralFilter(gray,5,6,6)

# Threshold the blurred image to get the black boundaries
_, thresh = cv2.threshold(blurred, 175, 255, cv2.THRESH_BINARY)

#cv2.imshow('thresh',thresh)

#input the end coordinate
a=5
b=5
height, width, _ = image.shape
dimension=int((height/a +width/b)/2)
x=z=dimension//2; #starting coordinate
arr=np.zeros((a,b));
for i in range(0,a):
    for j in range(0,b): #j for the column
        if(thresh[x+i*(2*x),x+j*(2*x)]==255):
            arr[i][j]=0 #0 for paths we can take
        else:
            arr[i][j]=1 # 1 for obstacles
print(arr)

#Breadth-First Search (BFS) algorithm
from collections import deque

# Sample input and print statement
grid = arr
k = 0

# Call the function to get the result
result_length, result_path = shortestPath(grid, k)

if result_length != -1:
    print("Shortest Path Length:", result_length)
    print("Shortest Path:")
    for x, y in result_path:
        print(f"({x+1}, {y+1})")
else:
    print("Destination is unreachable.")

#marking on image
from PIL import Image, ImageDraw
result_path= [list(t) for t in result_path]
result_path = [(2 * z*y + z, 2 * z*x + z) for x, y in result_path]

# Load the image
image_path = 'img2.jpg'
image = Image.open(image_path)

# Create a drawing object
draw = ImageDraw.Draw(image)

# Mark red spots on the image
for point in result_path:
    x, y = point  # Extract x and y components
    draw.ellipse([x - 4, y - 4, x + 4, y + 4], fill='red')

# Save or display the modified image
image.show() 

