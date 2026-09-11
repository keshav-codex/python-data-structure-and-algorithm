'''
Coordinate Tuple
Given a tuple of coordinate tuples:

points = ((2, 3), (5, 1), (4, 6), (1, 2))

Find the point having the largest x + y value.

Expected: (4, 6)

'''

def cordinate_finder(cordinate : tuple)-> None:
    maximum= sum(cordinate[0])
    max_index = 0

    for i in range(1,len(cordinate)):
        if sum(cordinate[i]) > maximum:
            maximum = sum(cordinate[i])
            max_index = i

    print(cordinate[max_index])

if __name__ == "__main__" :
    points = ((2, 3), (5, 1), (4, 6), (1, 2))
    cordinate_finder(points)
