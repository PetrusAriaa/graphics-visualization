from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path
import matplotlib.animation as animation

def draw_polygon(ax: Any, arr: np.ndarray):

    codes = [Path.MOVETO] + [Path.LINETO]*(len(arr)-2) + [Path.CLOSEPOLY]

    path = Path(arr, codes)
    pathpatch = PathPatch(path, facecolor='none', edgecolor='black')

    ax.plot()
    ax.add_patch(pathpatch)
    ax.set_title('A compound path')

    ax.set_box_aspect(1)    
    ax.autoscale()


def rotate(deg: float) -> np.ndarray:
    rad = deg*np.pi/180
    rotation_matrix = np.array([[np.cos(rad), -(np.sin(rad))], [np.sin(rad), np.cos(rad)]])
    return rotation_matrix


def transform_rotate(arr: np.ndarray, deg: float):
    R = rotate(deg)
    bottom_left = arr[0]
    bottom_right = arr[1]
    upper_right = arr[2]
    upper_left = arr[3]
    
    bottom_left_result = np.array([R[0][0]*bottom_left[0]+R[0][1]*bottom_left[1], R[1][0]*bottom_left[0]+R[1][1]*bottom_left[1]])
    bottom_right_result = np.array([R[0][0]*bottom_right[0]+R[0][1]*bottom_right[1], R[1][0]*bottom_right[0]+R[1][1]*bottom_right[1]])
    upper_right_result = np.array([R[0][0]*upper_right[0]+R[0][1]*upper_right[1], R[1][0]*upper_right[0]+R[1][1]*upper_right[1]])
    upper_left_result = np.array([R[0][0]*upper_left[0]+R[0][1]*upper_left[1], R[1][0]*upper_left[0]+R[1][1]*upper_left[1]])
    
    new_vertices = np.array([bottom_left_result, bottom_right_result, upper_right_result, upper_left_result, bottom_left_result])
    return new_vertices


    

def main():
    
    
    fig, ((ax1, ax2)) = plt.subplots(1,2)
    
    
    print("""Please input 4 points (x,y). Eg:
bottom_left: 2, 3
bottom_right: 5, 2
==================
          """)
    bottom_left = input("bottom_left: ")
    bottom_right = input("bottom_right: ")
    upper_right = input("upper_right: ")
    upper_left = input("upper_left: ")
    deg = float(input("rotation degree: "))
    
    bottom_left = bottom_left.split(',')
    bottom_right = bottom_right.split(',')
    upper_right = upper_right.split(',')
    upper_left = upper_left.split(',')
    
    bottom_left = np.array([int(bottom_left[0]), int(bottom_left[1])])
    bottom_right = np.array([int(bottom_right[0]), int(bottom_right[1])])
    upper_right = np.array([int(upper_right[0]), int(upper_right[1])])
    upper_left = np.array([int(upper_left[0]), int(upper_left[1])])
    
    vector = np.array([bottom_left, bottom_right, upper_right, upper_left, bottom_left])

    draw_polygon(ax1, vector)
    
    
    result = transform_rotate(vector, deg)
    draw_polygon(ax2, result)

    plt.show()
    

if __name__ == '__main__':
    main()