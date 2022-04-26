fuelDensity = 6.7

reserveWeight = 2900
mainOneFourWeight = 11000
mainTwoThreeWeight = 11000
forwardWeight = 4000
centerWeight = 20000
aftWeight = 2000
upperDeckWeight = 200
# arm
#=IF(B8=" ", " ", +num1*(q*2/f)^2+num2*(q*2/f)^1.5+9.81*(q*2/f)^0.5-num3*(q*2/f)+num4)
# Calculates the moment for any tank given a weight and arm
def tankMoment(w, arm):
    return round(w * arm / 1000, 1)


# Calculates the arm for either reserve tank given weight and fuel density
def reserveArmCalculation(w, d):
    num1 = -0.0002315
    num2 = 0.02154
    num3 = 0.6816
    num4 = 1007.68
    total = num1 * (w * 2 / d) ** 2 + num2 * (w * 2 / d) ** 1.5 + 9.81 * (w * 2 / d) ** 0.5 - num3 * (w * 2 / d) + num4
    return round(total, 1)


# num1*(B9*2/D4)^3.4-num2*(B9*2/D4)^2.4+num3*(B9*2/D4)^2-num4*(B9*2/D4)^1.6+num5)
# Calculates the arm for main tank 1 or 4 given weight and fuel density
def mainOneAndFourArmCalculation(w, d):
    num1 = 0.00000000004685
    num2 = 0.000001002
    num3 = 0.00003398
    num4 = 0.0002816
    num5 = 878.92
    weightByDensity = (w * 2 / d)
    total = num1 * weightByDensity ** 3.4 - num2 * weightByDensity ** 2.4 + num3 * weightByDensity ** 2 - num4 * weightByDensity ** 1.6 + num5
    return round(total, 1)

#  num1*(B10*2/D4)^3.5   +num2*(B10*2/D4)^3    -num3*(B10*2/D4)^2     +num4*(B10*2/D4)^0.5     +num5 )
# Calculates the arm for main tank 2 or 3 given weight and fuel density
def mainTwoAndThreeArmCalculation(w, d):
    num1 = -0.00000000001632
    num2 = 0.000000001656
    num3 = 0.000003255
    num4 = 0.1052
    num5 = 799.6
    weightByDensity = (w * 2 / d)
    total = num1 * weightByDensity ** 3.5 + num2 * weightByDensity ** 3 - num3 * weightByDensity ** 2 + num4 * weightByDensity ** 0.5 + num5
    return round(total, 1)



# -0.000003029*(B14/D4)^2.5+0.00018168*(B14/D4)^2+-0.134*(B14/D4)+555.16,
# Calculates the arm for forward body given weight and fuel density
def forwardBodyArmCalculation(w, d):
    if w / d <= 1231:
        num1 = -0.000003029
        num2 = 0.00018168
        num3 = -0.134
        num4 = 555.16
        weightByDensity = (w / d)
        total = num1 * weightByDensity ** 2.5 + num2 * weightByDensity ** 2 + num3 * weightByDensity + num4
        return round(total, 1)

# -0.00000003622*(B14/D4)^2.5+0.00005623*(B14/D4)^1.75-0.02903*(B14/D4)+528.28))
    else:
        num1 = -0.00000003622
        num2 = 0.00005623
        num3 = 0.02903
        num4 = 528.28
        weightByDensity = (w / d)
        total = num1 * weightByDensity ** 2.5 + num2 * weightByDensity ** 1.75 - num3 * weightByDensity + num4
        return round(total, 1)


# num1*(B15/D4)^5     -num2*(B15/D4)^2     -num3*(B15/D4)^0.25   +num4,
# Calculates the center wing arm given fuel weight and fuel density
def centerArmCalculation(w, d):
    if w / d <= 3692:
        num1 = 0.000000000000000008802
        num2 = 0.000000885
        num3 = 3.0868
        num4 = 767.61
        weightByDensity = (w / d)
        total = num1 * weightByDensity ** 5 - num2 * weightByDensity ** 2 - num3 * weightByDensity ** 0.25 + num4
        return round(total, 1)

# num1*(B15/D4)^3    +num2*(B15/D4)^2     -num3*(B15/D4)   +num4))
    else:
        num1 = -0.0000000001489
        num2 = 0.00000187
        num3 = 0.009244
        num4 = 753.32
        weightByDensity = (w / d)
        total = num1 * weightByDensity ** 3 + num2 * weightByDensity ** 2 - num3 * weightByDensity + num4
        return round(total, 1)





# Calculates aft body arm given fuel weight and density
# num1*(B16/D4)^2.5          +num2*(B16/D4)^2           +num3*(B16/D4)+num4
def aftArmCalculation(w, d):
    if w / d <= 769:
        num1 = -0.00000204
        num2 = 0.00009122
        num3 = 0.010346
        num4 = 1048.02
        weightByDensity = (w / d)
        total = num1 * weightByDensity ** 2.5 + num2 * weightByDensity ** 2 + num3 * weightByDensity + num4
        return round(total, 1)

# num1*(B16/D4)^1.25          -num2*(B16/D4)       +num3*(B16/D4)^0.75       +num4
    elif w / d < 5385:
        num1 = 0.00468
        num2 = 0.10557
        num3 = 0.641
        num4 = 1045.41
        weightByDensity = (w / d)
        total = num1 * weightByDensity ** 1.25 - num2 * weightByDensity + num3 * weightByDensity ** 0.75 + num4
        return round(total, 1)

    # num1*(B16/D4)^3          +num2*(B16/D4)^2         -num3*(B16/D4)+num4)))
    else:
        num1 = -0.00000001524
        num2 = 0.00026158
        num3 = 1.4964
        num4 = 3948.6
        weightByDensity = (w / d)
        total = num1 * weightByDensity ** 3 + num2 * weightByDensity ** 2 - num3 * weightByDensity + num4
        return round(total, 1)


# Calculates the arm of upper deck given fuel weight and density
# num1*(B17/D4)^3         -num2*(B17/D4)^2          +num3*(B17/D4)+num4)
def upperDeckArmCalculation(w, d):
    num1 = 0.000000000273
    num2 = 0.000002736
    num3 = 0.00741
    num4 = 1408.93
    weightByDensity = (w / d)
    total = num1 * weightByDensity ** 3 - num2 * weightByDensity ** 2 + num3 * weightByDensity + num4
    return round(total, 1)






reserveArm = reserveArmCalculation(reserveWeight, fuelDensity)
reserveMoment = tankMoment(reserveWeight, reserveArm)

oneFourArm = mainOneAndFourArmCalculation(mainOneFourWeight, fuelDensity)
oneFourMoment = tankMoment(mainOneFourWeight, oneFourArm)

twoThreeArm = mainTwoAndThreeArmCalculation(mainTwoThreeWeight, fuelDensity)
twoThreeMoment = tankMoment(mainTwoThreeWeight, twoThreeArm)

forwardArm = forwardBodyArmCalculation(forwardWeight, fuelDensity)
forwardMoment = tankMoment(forwardWeight, forwardArm)

centerArm = centerArmCalculation(centerWeight, fuelDensity)
centerMoment = tankMoment(centerWeight, centerArm)\

aftArm = aftArmCalculation(aftWeight, fuelDensity)
aftMoment = tankMoment(aftWeight, aftArm)

upperDeckArm = upperDeckArmCalculation(upperDeckWeight, fuelDensity)
upperDeckMoment = tankMoment(upperDeckWeight, upperDeckArm)

print(f"Reserve Arm: {reserveArm}\n"
      f"Reserve Moment: {reserveMoment}\n"
      f"Main 1 and 4 Arm: {oneFourArm}\n"
      f"Main 1 and 4 Moment: {oneFourMoment}\n"
      f"Main 2 and 3 Arm: {twoThreeArm}\n"
      f"Main 2 and 3 Moment: {twoThreeMoment}\n"
      f"Forward Arm: {forwardArm}\n"
      f"Forward Moment: {forwardMoment}\n"
      f"Center Arm: {centerArm}\n"
      f"Center Moment: {centerMoment}\n"
      f"Aft Arm: {aftArm}\n"
      f"Aft Moment: {aftMoment}\n"
      f"Upper Deck Arm: {upperDeckArm}\n"
      f"Upper Deck Moment = {upperDeckMoment}")
