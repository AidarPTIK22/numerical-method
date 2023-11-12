import numpy as np

# Function to calculate velocity using the given formula
def calculate_velocity(t):
    g = 9.8  # gravitational constant (m/s^2)
    m = 68.1  # mass of the parachutist (kg)
    c = 12.5  # drag coefficient (kg/s)

    # Calculate velocity using the given formula
    v = (g * m) / c * (1 - np.exp(- (c / m) * t))

    return v

# Trapezoidal rule for numerical integration
def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    result = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        result += func(a + i * h)
    result *= h
    return result

# Simpson's rule for numerical integration
def simpsons_rule(func, a, b, n):
    h = (b - a) / n
    result = func(a) + func(b)
    for i in range(1, n, 2):
        result += 4 * func(a + i * h)
    for i in range(2, n-1, 2):
        result += 2 * func(a + i * h)
    result *= h / 3
    return result

# Unequally spaced data
def unequally_spaced_data():
    # Example unequally spaced data
    time_values = np.array([0, 2, 5, 8, 10])  # time values in seconds
    velocity_values = calculate_velocity(time_values)

    # Perform numerical integration using numpy trapz function for unequally spaced data
    area_trapz = np.trapz(velocity_values, x=time_values)

    return area_trapz

# Test the trapezoidal rule and Simpson's rule
a = 0  # Start time
b = 10  # End time
n = 1000  # Number of intervals

# Calculate the area under the velocity-time curve using the trapezoidal rule
area_trapezoidal = trapezoidal_rule(calculate_velocity, a, b, n)

# Calculate the area under the velocity-time curve using Simpson's rule
area_simpsons = simpsons_rule(calculate_velocity, a, b, n)

# Calculate the area under the velocity-time curve for unequally spaced data
area_unequally_spaced = unequally_spaced_data()

# Print the results
print(f"Area under the curve using Trapezoidal rule: {area_trapezoidal} m")
print(f"Area under the curve using Simpson's rule: {area_simpsons} m")
print(f"Area under the curve for unequally spaced data: {area_unequally_spaced} m")
