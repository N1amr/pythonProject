def sort(array):
	arr = []
	sz = 0
	for x in array:
		arr.append(x)
		sz += 1

		parent = sz - 1
		while True:
			i = parent
			parent = (i - 1) // 2

			if not (i > 0 and arr[i] > arr[parent]):
				break

			parent = (i - 1) // 2
			tmp = arr[i]
			arr[i] = arr[parent]
			arr[parent] = tmp

	while sz > 0:
		tmp = arr[0]
		arr[0] = arr[sz - 1]
		arr[sz - 1] = tmp

		sz -= 1

		j = 0
		while True:
			i = j
			child1 = i * 2 + 1
			child2 = i * 2 + 2

			if not ((child1 < sz and arr[i] < arr[child1]) or (child2 < sz and arr[i] < arr[child2])):
				break

			j = child2 if child2 < sz and arr[child2] > arr[child1] else child1
			tmp = arr[i]
			arr[i] = arr[j]
			arr[j] = tmp

	return arr
