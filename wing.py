#!/usr/bin/python

from opyscad import *


delimiter = ';'
fn = 'w1.csv'
zoom = 30
wing_len = 150
scale = 2
scale_offset = 0


def load_file(fn):
	f = open(fn, 'r')
	if not f:
		return None

	res = f.readlines()

	res = [map(float, l.split(delimiter)) for l in res]

	f.close()
	return res

def profile_polygon(profile, zoom):
	poly_u = []
	poly_d = []

	for x, y_u, y_d in profile:
		poly_u.append([-x * zoom, y_u * zoom])
		poly_d.append([-x * zoom, y_d * zoom])

	poly_d.reverse()
	poly = poly_u + poly_d[1:]

	return polygon(poly)

def main():
	profile = load_file(fn)
	if not profile:
		print 'Profile loading error'
		return

	poly = profile_polygon(profile, zoom)
	poly2 = profile_polygon(profile, zoom/2)

	poly <<= [scale_offset, 0, 0]

	wing = linear_extrude(wing_len, scale = 0.5) (poly)

	wing <<= [-scale_offset, 0, 0]

	wing /= [90, 0, 0]

	wing <<= [0, -10, 0]
	wing += (wing | [0, 1, 0])

	wing.save('wing.scad')


if __name__ == '__main__':
	main()



