def dot_in_triangle(d, x, y):
    '''
    Функция вычисляет положение точки с координатами x, y
    относительно треугольника с заданной длиной катета d
    '''
    for i in range(d+1):
        for j in range(d-i+1):
            if (x, y) == (i, j):
                return 0
    
    dist_a = (x ** 2 + y ** 2) ** 0.5
    dist_b = ((d - x) ** 2 + y ** 2) ** 0.5
    dist_c = (x ** 2 + (d - y) ** 2) ** 0.5
    min_ = min((dist_a, dist_b, dist_c))
    if min_ == dist_a:
        return 1
    elif min_ == dist_b:
        return 2
    elif min_ == dist_c:
        return 3

if __name__ == "__main__":
    d, x, y = map(int, input("Введите три значения через пробел (длину катета, X, Y): ").split())
    print(dot_in_triangle(d, x, y))