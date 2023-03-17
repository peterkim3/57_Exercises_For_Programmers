# https://en.wikipedia.org/wiki/Blood_alcohol_content
# EBAC in SI metrics
# BAC = (A × 5.14 /W × r) − 0.015 × H
# 80 kg male drinking 2 drinks of 14 grams (0.014 kg) each, in two hours:

W = 80
A = 2 * 0.014
H = 2
r = 0.68

limit = 0.08
ebac = A / (r * W) * 100 - (0.015 * H)

print(f"Your BAC is {ebac}\n It is Okay for you to drive.") if ebac < limit else print(f"Your BAC is {ebac}\n It is not legal for you to drive.")


"""
Challenges
Develop this as a mobile application that makes it easy
to record each drink, updating the BAC each time a drink is entered.
"""