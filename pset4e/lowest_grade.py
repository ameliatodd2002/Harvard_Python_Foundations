def remove_lowest(grade_list):
    if grade_list == []:
        return []
    elif grade_list == [grade_list[0]]:
        return grade_list
    else:
        new_grade_list = []
        for i in range(len(grade_list)):
            new_grade_list.append(grade_list[i])
        minimum = min(new_grade_list)
        new_grade_list.remove(minimum)
        return new_grade_list

def main():
    x = [23, 90, 47, 55, 88]
    a = remove_lowest(x)
    b = remove_lowest([85])
    c = remove_lowest([])
    d = remove_lowest([59, 92, 93, 47, 88, 47])
    print("x =", x)
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)

if __name__ == '__main__':
    main()

