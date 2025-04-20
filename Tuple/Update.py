x = ("Bmw", "bugatti", "suzuki")
y = list(x)
y[1] = "Mercedes"
x = tuple(y)
print(x)

#output ('Bmw', 'Mercedes', 'suzuki')
