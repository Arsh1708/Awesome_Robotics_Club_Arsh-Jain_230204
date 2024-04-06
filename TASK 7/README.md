<h1>Path Planning Algorithm</h1><br>
We have to find the minimum number of steps to reach the bottom right coordinate in the given grid image, starting from (1,1).We also have to print the path planned. The process involves two tasks.<br>
<h2>Converting the image to a 2D numpy array</h2><br>
The dimensions of each grid box is calculated using the total size of the image and the number of rows and columns.The image is then converted to grayscale and then into binary using the threshold command in opencv.Therefore, the blue and yellow boxes turn to black and white respectively.The start position is from the center coordiante of the box at (1,1). Iterating through each box, 1 is assigned to the boxes which aren't allowed for traversal(black) and 0 for the allowed ones(white). This is stored in a 2D numpy array.
<br>
<h2>Breadth First Search Algorithm</h2><br>
The shortestPath function calculates the shortest path in a grid from the top-left corner to the bottom-right corner.
The algorithm explores all nodes at each level and is memoized as we keep track of the boxes we have already visited.The algorithm starts at the top left corner and explores neighbouring nodes in all 4 directions if not visited earlier.After each level of exploration the 'step' variable is increased by 1.It stops until the bottom right corner is reached.The coordinates of the shortest path are appended in the path variable of the queue and at the end only those coordiantes are printed which are valid(not 1).
