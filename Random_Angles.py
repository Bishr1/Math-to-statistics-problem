import random

I = 0
P = 0
O = 0

for Times in range(100000):
    a = random.uniform(0, 180)

    if a < 90:
        b = random.uniform(0, 180)

        if b >= 90:
            a = random.uniform(0, 180 - b)
    else:
        b = random.uniform(0, 180 - a)

    c = 180 - a - b

    #print('The triangle', Times + 1,':', '       ', 'a =', a, '     ', 'b =', b, '     ', 'c =', c)

    if a < 90 and b < 90 and c < 90:
        I = I + 1

        #print('Times of X landed in the inside:', I)
        #print('')
    elif a == 90 or b == 90 or c == 90:
        P = P + 1

        #print('Times of X landed in the perimeter:', P)
        #print('')
    elif a > 90 or b > 90 or c > 90:
        O = O + 1

        #print('Times of X landed in the outside:', O)
        #print('')

    #print("The ratio between times of X landed inside the triangle and not is:", I / (I + P + O))
    #print("The ratio between times of X landed in the perimeter and not is:", P / (I + P + O))
    #print("The ratio between times of X landed outside the triangle and not is:", O / (I + P + O))
    #print('')
    #print('')

print("The ratio between times of X landed inside the triangle and not is:", I / (I + P + O))
print("The ratio between times of X landed in the perimeter and not is:", P / (I + P + O))
print("The ratio between times of X landed outside the triangle and not is:", O / (I + P + O))
