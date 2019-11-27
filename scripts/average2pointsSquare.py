###############################################################################
## File Name: average2pointsSquare.py                                        ##
## Description: Find out the average distance between 2 points in a square   ##
###############################################################################
import numpy as np
import random
import matplotlib.pyplot as plt

realValue = 0.5214

def distance(x, y):
    distance = np.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
    return distance;
    
def create_points():
    x = np.array([random.random(), random.random()])
    return x;


    
np_averageDistance = np.array([])
np_points = np.array([])

# Number of points used to calculate the distance in first iteration
points = 10
np_distances = np.array([])
while points <= 100000:
    np_points = np.append(np_points, points)
    j = 0
    while j < points:
        np_x = create_points()
        np_y = create_points()
        # Check 'norm' for distance between 2 points
        np_distances = np.append(np_distances, distance(np_x, np_y))
        j += 1
    
    np_averageDistance = np.append(np_averageDistance, np.mean(np_distances))
    
    # Each iteration has x10 points
    points = 10 * points

print('The average distance calculated between 2 random points in a square is', np_averageDistance[-1])
print('The real average distance between 2 random points in a square is', realValue)

np_difference = abs(np_averageDistance - realValue)

plt.scatter(np_points, np_difference)
plt.xscale('log')
plt.xlabel('Points')
plt.ylabel('Deviation')
plt.title('Deviation from real value')
plt.show()
