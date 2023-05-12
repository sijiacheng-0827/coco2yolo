line = (1.234, 2, 3, 4.6345, None)
line = [1 if x is None else x for x in line]
line = tuple(line)
b = ('%g ' * len(line)).rstrip() % line
print(b)