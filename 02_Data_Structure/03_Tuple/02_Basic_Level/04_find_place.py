'''
Given:

points = {
    (10, 20): "Point A",
    (30, 40): "Point B",
    (50, 60): "Point C"
}

Given a coordinate:

coordinate = (30, 40)

find and print its associated value.
'''


def find_place(points: dict , coordinate:tuple) -> None:
		print(points.get(coordinate))

if __name__ == "__main__":
	points = {
	(10, 20): "Point A",
	(30, 40): "Point B",
	(50, 60): "Point C"
	}

	coordinate = (30, 40)

	find_place(points, coordinate)