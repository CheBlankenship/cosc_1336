
# 1.Create a table using a two-dimensional array that stores a Fahrenheit temperate and the equivalent Celsius temperature.
#   Use the following range of Fahrenheit temperatures
#   -10 through 100 in increments of 10, thus the temperatures will be
#   -10, 0, 10, 20, 30, 40, 50 …and so on

# Return type: integer.
## F to C ##
def FahToCel(f2c):
    return int((f2c - 32) * 5 // 9)

## Gal to L ##
def GalToLit(galToL):
    return int(galToL * 3.9)

## Lb to Kg ##
def PoundsToKg(poundToKg):
    return int(poundToKg * 0.45)

## Inch to cm ##
def InchesToCm(inchesToCm):
    return int(inchesToCm * 2.54)

## Mil to Km ##
def MilesToKm(m2k):
    return int(m2k * 1.6)


f_and_c     = [[], []]
fahrenheit  = []
celsius     = []
for num in range(-10, 101, 10):
    fahrenheit.append(num)
    celsius.append(FahToCel(num))
# Store fahrenheit into index 0 & celsius into index 1.
f_and_c[0] = fahrenheit
f_and_c[1] = celsius

# 2.Display the contents of the list.
print("F to C   : ", f_and_c)


# 3.Similarly create tables/lists for the following (starting at 0 through 100 in increments of 10
# a.Miles to kilometers
m_and_k     = [[], []]
miles       = []
kilometers  = []
for num in range(0, 101, 10):
    miles.append(num)
    kilometers.append(MilesToKm(num))
# Store into the two-dimensional array.
m_and_k[0] = miles
m_and_k[1] = kilometers
print("Mil to km: ", m_and_k)

# b.Gallons to liters
g_and_l     = [[], []]
gallons     = []
liters      = []
for num in range(0, 101, 10):
    gallons.append(num)
    liters.append(GalToLit(num))
# Store into the two-dimensional array.
g_and_l[0] = gallons
g_and_l[1] = liters
print("Gal to L : ", g_and_l)

# c.Pounds to kilograms
l_and_k     = [[], []]
pounds      = []
kilograms   = []
for num in range(0, 101, 10):
    pounds.append(num)
    kilograms.append(PoundsToKg(num))
# Store into the two-dimensional array.
l_and_k[0] = pounds
l_and_k[1] = kilograms
print("L to kg  : ", l_and_k)

# d.Inches to centimeters
i_and_c     = [[], []]
inches      = []
centimeters = []
for num in range(0, 101, 10):
    inches.append(num)
    centimeters.append(InchesToCm(num))
# Store into the two-dimensional array.
i_and_c[0] = inches
i_and_c[1] = centimeters
print("Inc to cm: ", i_and_c)
