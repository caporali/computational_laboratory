#output testuale
def text_output(begin, route, f_begin, f_route):
	print("Start route: ", begin.tolist())
	print()
	print("Final route: ", [int(i) for i in route.tolist()])
	print()
	print("Start cost: ", f_begin)
	print()
	print("Final cost: ", f_route)