import numpy as np
from skimage import measure

def getBigestIsland(grid):
    labels = measure.label(grid, connectivity=2)
    print (labels)

filepath = 'dataset2.txt'

if __name__ == "__main__":
    grid = np.array([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
                     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                     [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0],
                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]])
    getIsland=getIsland(grid)
    axRow = max(np.getIsland(grid))
    print(maxRow)