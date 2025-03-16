print("Welcome, This is a simple interest calculator")  

p, r, t = input("Enter the principal amount, rate of interest, and time period in years: ").split()
p = float(p)
r = float(r)
t = int(t)

if p <= 0 or r <= 0 or t <= 0:
    print("Please enter a valid input")
else:
    si = (p * r * t) / 100
    print("The simple interest is:", si)

# Compound Interest  
print("Welcome, This is a compound interest calculator")  

p, r, t = input("Enter the principal amount, rate of interest, and time period in years: ").split()
p = float(p)
r = float(r) / 100  # Convert percentage to decimal
t = int(t)
n = int(input("Enter the number of times interest is compounded per year: "))

a = p * (1 + (r / n)) ** (n * t)
ci = a - p  

if p <= 0 or r <= 0 or t <= 0 or n <= 0:
    print("Please enter a valid input")  
else:  
    print("The compound interest is:", ci)  

# Annuity Plan  
print("Welcome, This is an Annuity plan calculator!")  

pmt = float(input("Enter the principal amount: "))  
r = float(input("Enter the rate of interest (in percentage): ")) / 100  # Convert percentage to decimal
n = int(input("Enter the number of times the interest is compounded in a year: "))  
t = int(input("Enter the time period in years: "))

a = pmt * (((1 + r / n) ** (n * t) - 1) / (r / n))  
print("Your Annuity plan is:", a)

  