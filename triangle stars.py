def print_triangle(h):
    for i in range(h):
        spaces = " " * (h - i)
        stars = "*" * (i+1)
        if i >= 1:
            stars += "" + "*" * i
        print(f"{spaces}{stars}")

triangle_height =12
print_triangle(triangle_height)