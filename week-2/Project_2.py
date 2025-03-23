def solve_quadratic(a, b, c):
    D = b**2 - 4*a*c
    if D >= 0:
        root1 = (-b + D**0.5) / (2*a)
        root2 = (-b - D**0.5) / (2*a)
        return root1, root2
    else:
        real_part = -b / (2*a)
        imaginary_part = (abs(D)**0.5) / (2*a)
        return (real_part, imaginary_part), (real_part, -imaginary_part)

def solve_cubic(a, b, c, d):
    def cubic_root(x):
        return x**(1/3) if x >= 0 else -(-x)**(1/3)
    
    f = ((3*c/a) - (b**2/a**2)) / 3
    g = ((2*b**3/a**3) - (9*b*c/a**2) + (27*d/a)) / 27
    h = (g**2 / 4) + (f**3 / 27)
    
    if h > 0:
        R = -(g/2) + (h**0.5)
        S = cubic_root(R)
        T = -(g/2) - (h**0.5)
        U = cubic_root(T)
        root1 = S + U - (b/(3*a))
        return root1,
    elif h == 0 and f == 0 and g == 0:
        root = -cubic_root(d/a)
        return root,
    else:
        i = ((g**2 / 4) - h)**0.5
        j = cubic_root(i)
        k = (1 / 3) * (3.141592653589793 * 2) / 3
        L = j * (-1)
        M = j * (1)
        root1 = (2*j) - (b/(3*a))
        root2 = (L * 1.7320508075688772) - (b/(3*a))
        root3 = (M * 1.7320508075688772) - (b/(3*a))
        return root1, root2, root3

def solve_quartic(a, b, c, d, e):
    roots = []
    for i in range(-1000, 1001):
        if i != 0 and a * i**4 + b * i**3 + c * i**2 + d * i + e == 0:
            roots.append(i)
    return roots if roots else "Complex roots (not solved without imports)"

def main():
    print("Choose the type of equation to solve:")
    print("1. Quadratic (Ax² + Bx + C = 0)")
    print("2. Cubic (Ax³ + Bx² + Cx + D = 0)")
    print("3. Quartic (Ax⁴ + Bx³ + Cx² + Dx + E = 0)")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        a = float(input("Enter coefficient A: "))
        b = float(input("Enter coefficient B: "))
        c = float(input("Enter coefficient C: "))
        roots = solve_quadratic(a, b, c)
    elif choice == "2":
        a = float(input("Enter coefficient A: "))
        b = float(input("Enter coefficient B: "))
        c = float(input("Enter coefficient C: "))
        d = float(input("Enter coefficient D: "))
        roots = solve_cubic(a, b, c, d)
    elif choice == "3":
        a = float(input("Enter coefficient A: "))
        b = float(input("Enter coefficient B: "))
        c = float(input("Enter coefficient C: "))
        d = float(input("Enter coefficient D: "))
        e = float(input("Enter coefficient E: "))
        roots = solve_quartic(a, b, c, d, e)
    else:
        print("Invalid choice.")
        return
    
    print("The roots of the equation are:", roots)
    
if __name__ == "__main__":
    main()