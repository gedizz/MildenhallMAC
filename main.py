#!C:\Users\Aegis\AppData\Local\Programs\Python\Python310\python.exe
#!/usr/bin/env python3

# Shebang to be added to my windows.
#!C:\Users\Aegis\AppData\Local\Programs\Python\Python310\python.exe

import cgitb
import cgi
from string import Template
import calc

cgitb.enable()
print("Content-Type: text/html;charset=utf-8")
print()  # <----------- additional newline for header/body separation.
# <meta http-equiv="refresh" content="60" >
# Below is the return to other parts of the website

# Receiving data from form after Calculate button is pressed. Used to calculate and update MAC
form = cgi.FieldStorage()

data = {
    "reserve1": form.getvalue("1reserve"),
    "main1": form.getvalue("1main"),
    "main2": form.getvalue("2main"),
    "forwardbody": form.getvalue("forwardbody"),
    "centerwing": form.getvalue("centerwing"),
    "aftbody": form.getvalue("aftbody"),
    "upperdeck": form.getvalue("upperdeck"),
    "main3": form.getvalue("3main"),
    "main4": form.getvalue("4main"),
    "reserve4": form.getvalue("4reserve"),
    "basicweight": form.getvalue("basicweight"),
    "fuelweight": form.getvalue("fuelweight"),
    "basicmoment": form.getvalue("basicmoment"),
    "fueldensity": form.getvalue("fueldensity")
}

totalWeightCalculation = 0.0
totalFuelWeightCalculation = 0.0
# If no data is received (likely first going to site) then set all values to 0 so we dont accidentally get NoneType
for x in data:
    if data[x] is None and x != "fueldensity":
        data[x] = float(1)
    elif x == "fueldensity" and data[x] == 6.7:
        data[x] = "6.7"
    elif x == "fueldensity" and data[x] is None:
        data[x] = "6.7"

    if x != "basicweight" and x != "fuelweight" and x != "basicmoment" and x != "fueldensity":
        totalFuelWeightCalculation += float(data[x])


totalWeightCalculation += totalFuelWeightCalculation
totalWeightCalculation += float(data["basicweight"])




# reserve1 = form.getvalue('1reserve')
# main1 = form.getvalue('1main')
# main2 = form.getvalue('2main')
# forwardBody = form.getvalue('forwardbody')
# aftBody = form.getvalue('aftbody')
# upperDeck = form.getvalue('upperdeck')
# main3 = form.getvalue('3main')
# main4 = form.getvalue('4main')
# reserve4 = form.getvalue('4reserve')

# <meta name="viewport" content="width=device-width, initial-scale=1.0">


# Below is all HTML
html = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta name="viewport" content="width=device-width"/>
    <link rel="stylesheet" href="stylesheet.css"/>
    <link rel="icon" type="image/x-icon" href="favicon.ico">
    <meta charset="UTF-8">
    <title>Mildenhall MAC</title>

</head>


<body>



    <div id="headings">
        <h1>Mil<img style="margin-bottom:0px; margin-left:1px;" src="fav32.png" height="22" width="16" alt="logo"/>enhall %MAC Calculator</h1>
        <hr id="solid">
        <h2><em>Integrity First - Service Before Self - Excellence In All We Do</em></h2>
    </div>


    <div class="topnav" id="myTopnav">
      <a href="main.py" class="active">Home</a>
      <a href="privacy.html">Privacy</a>
      <a href="support.html">Support</a>
    </div>

    <div class="textarea">

        <!-- Hidden form so we can bind input boxes without showing an entire form -->
        <form action="main.py" id="inputdata"><input type="hidden" name="id" value="1" method="get"/></form>

        <div class="cell" id="fwd">
            <h3>Forward Body</h3>
            <input form="inputdata" type="text" name="forwardbody" value="$fwd">
        </div>


        <div class="cell" id="onereserve">
            <h3>#1 Reserve</h3>
            <input form="inputdata" type="text" name="1reserve" value="$r1"/>
        </div>
        <div class="cell" id="onemain">
            <h3>#1 Main</h3>
            <input form="inputdata" type="text" name="1main" value="$m1"/>
        </div>


        <div class="cell" id="twomain">
            <h3>#2 Main</h3>
            <input form="inputdata" type="text" name="2main" value="$m2"/>
        </div>
        <div class="cell" id="centerwing">
            <h3>Center Wing</h3>
            <input form="inputdata" type="text" name="centerwing" value="$center"/>
        </div>
        <div class="cell" id="aftbody">
            <h3>Aft Body</h3>
            <input form="inputdata" type="text" name="aftbody" value="$aft"/>
        </div>
        <div class="cell" id="upperdeck">
            <h3>Upper Deck</h3>
            <input form="inputdata" type="text" name="upperdeck" value="$up"/>
        </div>

        <div class="cell" id="threemain">
            <h3>#3 Main</h3>
            <input form="inputdata" type="text" name="3main" value="$m3"/>
        </div>
        <div class="cell" id="fourmain">
            <h3>#4 Main</h3>
            <input form="inputdata" type="text" name="4main" value="$m4"/>
        </div>
        <div class="cell" id="fourreserve">
            <h3>#4 Reserve</h3>
            <input form="inputdata" type="text" name="4reserve" value="$r4"/>
        </div>

    </div>




    <div class="resultbox">
        <div class="col">

            <div class="leftrow">
                <h3>Basic Weight</h3>
                <input form="inputdata" type="text" name="basicweight" value="$basicWeight"/>
            </div>
            <div class="leftrow">
                <h3>Basic Moment</h3>
                <input form="inputdata" type="text" name="basicmoment" value="$basicMoment"/>
            </div>
            <div class="leftrow">
                <h3>Fuel Density</h3>
                <input form="inputdata" type="text" name="fueldensity" value="$fuelDensity"/>
            </div>

        </div>



        <div class="col">
            <div class="middlerow">
                <h1><u>Instructions:</u></h1>
                <p>Enter fuel load</p>
                <p>Enter basic weight, moment and fuel density</p>
                <p>Press calculate</p>
                <p style="color:red;">Please use only whole numbers or decimals.</p>
                <form action="main.py">
                    <input type="submit" value="Reset" />
                    <input type="submit" form="inputdata" value="Calculate">
                </form>
            </div>

        </div>


        <div class="col">


            <div class="rightrow">
                <h3>Total Fuel Weight:</h3>
                <a>$totalFuel</a>
            </div>
            <div class="rightrow">
                <h3>Total Weight:</h3>
                <a>$totalWeight</a>
            </div>
            <div class="rightrow">
                <h3>Final Arm:</h3>
                <a>$finalArm</a>
            </div>
            <div class="rightrow">
                <h3>Total Moment:</h3>
                <a>$totalMoment</a>
            </div>
            <div class="rightrow">
                <h3>%MAC (+-0.5%):</h3>
                <a>$finalCG</a>
            </div>


        </div>

    </div>





</body>
    <footer class="footer">Designed by A1C Geditz and Dylan Williams</footer>
</html>

"""
density = data["fueldensity"]

reserveOneArm = calc.reserveArmCalculation(data["reserve1"], density)
reserveOneMoment = calc.tankMoment(data["reserve1"], reserveOneArm)

mainOneArm = calc.mainOneAndFourArmCalculation(data["main1"], density)
mainOneMoment = calc.tankMoment(data["main1"], mainOneArm)

mainTwoArm = calc.mainTwoAndThreeArmCalculation(data["main2"], density)
mainTwoMoment = calc.tankMoment(data["main2"], mainTwoArm)

forwardArm = calc.forwardBodyArmCalculation(data["forwardbody"], density)
forwardMoment = calc.tankMoment(data["forwardbody"], forwardArm)

centerArm = calc.centerArmCalculation(data["centerwing"], density)
centerMoment = calc.tankMoment(data["centerwing"], centerArm)

aftArm = calc.aftArmCalculation(data["aftbody"], density)
aftMoment = calc.tankMoment(data["aftbody"], aftArm)

upperDeckArm = calc.upperDeckArmCalculation(data["upperdeck"], density)
upperDeckMoment = calc.tankMoment(data["upperdeck"], upperDeckArm)

mainThreeArm = calc.mainTwoAndThreeArmCalculation(data["main3"], density)
mainThreeMoment = calc.tankMoment(data["main3"], mainThreeArm)

mainFourArm = calc.mainOneAndFourArmCalculation(data["main4"], density)
mainFourMoment = calc.tankMoment(data["main4"], mainFourArm)

reserveFourArm = calc.reserveArmCalculation(data["reserve4"], density)
reserveFourMoment = calc.tankMoment(data["reserve4"], reserveFourArm)

totalMoment = reserveOneMoment + mainOneMoment + mainTwoMoment + forwardMoment + centerMoment + aftMoment + upperDeckMoment + mainThreeMoment + mainFourMoment + reserveFourMoment
totalMoment += float(data["basicmoment"])

finalArm = totalMoment*1000 / totalWeightCalculation
finalCG = (finalArm - 786.2) / 2.419

if round(finalCG, 1) == 58.3 and totalFuelWeightCalculation == 10.0:
    finalCG = 1.0
    overOrUnder = "Inside Limit"
    overOrUnderColor = "#2B8C2E"
else:
    if finalCG > 37 or finalCG < 0:
        overOrUnder = "Outside Limit"
        overOrUnderColor = "#D63714"
    else:
        overOrUnder = "Inside Limit"
        overOrUnderColor = "#2B8C2E"

html_replaced = Template(html).safe_substitute(
    r1="%s" % (data["reserve1"]),
    m1="%s" % (data["main1"]),
    m2="%s" % (data["main2"]),
    fwd="%s" % (data["forwardbody"]),
    center="%s" % (data["centerwing"]),
    aft="%s" % (data["aftbody"]),
    up="%s" % (data["upperdeck"]),
    m3="%s" % (data["main3"]),
    m4="%s" % (data["main4"]),
    r4="%s" % (data["reserve4"]),

    basicMoment="%s" % (data["basicmoment"]),
    basicWeight="%s" % (data["basicweight"]),
    fuelWeight="%s" % (data["fuelweight"]),
    fuelDensity="%s" % (data["fueldensity"]),

    totalWeight="%s" % totalWeightCalculation,
    finalArm="%s" % round(finalArm, 1),
    totalMoment="%s" % round(totalMoment, 1),
    finalCG="%s" % round(finalCG, 1),
    totalFuel="%s" % totalFuelWeightCalculation,

    overOrUnder="%s" % overOrUnder,
    overOrUnderColor="%s" % overOrUnderColor)

print(html_replaced)


