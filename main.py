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
<html>
<title>Mildenhall MAC</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>

table {
  border:1px solid black;
  font-size: 1vw
}

.specialtable {
    border:1px solid black;
}

th {
border:1px solid black;
}

.special {
border:0px;
}

td {
  width: 14.2%;
  border:1px solid black;
}

.specialtd {
  border:1px solid black;
}

input {
margin-top: 5px;
margin-bottom: 5px;
}

footer {
width:100%;
}

.column {
  float: left;
  width: 33.33%;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
</style>
<body>

<h2 align=center >Mildenhall %MAC Calculator</h2>




<!-- Main Table -->
<table style="width:100%">


  <tr>
    <td class="special"></td>
    <td class="special"></td>
    <td class="special"></td>
    <th style="background-color:#ADADAA">Forward Body</th>
    <td class="special"></td>
    <td class="special"></td>
    <td class="special"></td>
  </tr>

  <tr>
    <td class="special"></td>
    <td class="special"></td>
    <td class="special"></td>
    <td align=center><input form="form1" type="text" name="forwardbody" value="$fwd" /></td>
    <td class="special"></td>
    <td class="special"></td>
    <td class="special"></td>
  </tr>


  <tr style="background-color:#ADADAA">
    <th>#1 Reserve</th>
    <th>#1 Main</th>
    <th>#2 Main</th>
    <th>Center Wing</th>
    <th>#3 Main</th>
    <th>#4 Main</th>
    <th>#4 Reserve</th>
  </tr>


  <form action="main.py" id="form1"><input type="hidden" name="id" value="1" method="get"/></form>

  <tr>
    <td align=center><input form="form1" type="text" name="1reserve" value="$r1" /></td>
    <td align=center><input form="form1" type="text" name="1main" value="$m1" /></td>
    <td align=center><input form="form1" type="text" name="2main" value="$m2" /></td>
    <td align=center><input form="form1" type="text" name="centerwing" value="$center" /></td>
    <td align=center><input form="form1" type="text" name="3main" value="$m3" /></td>
    <td align=center><input form="form1" type="text" name="4main" value="$m4" /></td>
    <td align=center><input form="form1" type="text" name="4reserve" value="$r4" /></td>
  </tr>


  <tr>
    <td class="special"></td>
    <td class="special"></td>
    <td class="special"></td>
    <th style="background-color:#ADADAA">Aft Body</th>
    <td class="special"></td>
    <td class="special"></td>
    <td class="special"></td>
  </tr>

  <tr>
    <td class="special"></td>
    <td class="special"></td>
    <td class="special"></td>
    <td align=center><input form="form1" type="text" name="aftbody" value="$aft" /></td>
    <td class="special"></td>
    <td class="special"></td>
    <td class="special"></td>
  </tr>

  <tr>
    <td class="special"></td>
    <td class="special"></td>
    <td class="special"></td>
    <th style="background-color:#ADADAA">Upper Deck</th>
    <td class="special"></td>
    <td class="special"></td>
    <td class="special"></td>
  </tr>

  <tr>
    <td class="special"></td>
    <td class="special"></td>
    <td class="special"></td>
    <td align=center><input form="form1" type="text" name="upperdeck" value="$up" /></td>
    <td class="special"></td>
    <td class="special"></td>
    <td class="special"></td>
  </tr>

</table>




<!-- Aircraft Weights -->
<div class="row">
    <div class="column">


        <table>



          <tr>
            <td style="background-color:#ADADAA">Basic Weight</td>
            <td align=center><input form="form1" type="text" name="basicweight" value="$basicWeight" /></td>
          </tr>


          <tr>
            <td style="background-color:#ADADAA">Basic Moment</td>
            <td align=center><input form="form1" type="text" name="basicmoment" value="$basicMoment" /></td>
          </tr>




          <tr>
            <td style="background-color:#ADADAA">Fuel Density</td>
            <td align=center><input form="form1" type="text" name="fueldensity" value="$fuelDensity" /></td>
          </tr>

        </table> 

    </div>



<!-- space in between -->   
    <div class="column">

        <table style="border:0px;">

          <tr>
            <td class="special"></td>
          </tr>

        </table> 
    </div>



<!-- Result Table -->   

    <div align=right class="column">


        <table>

          <tr>
            <td colspan="2" style="background-color:#ADADAA">Total Fuel Weight:</td>
            <td>$totalFuel</td>
          </tr>
          
          <tr>
            <td colspan="2" style="background-color:#ADADAA">Total Weight:</td>
            <td>$totalWeight</td>
          </tr>


         <tr>
            <td colspan="2" style="background-color:#ADADAA">Final Arm:</td>
            <td>$finalArm</td>
         </tr>


          <tr>
            <td colspan="2" style="background-color:#ADADAA">Total Moment:</td>
            <td>$totalMoment</td>
          </tr>

          <tr>
            <td style="background-color:#ADADAA">%MAC (+-0.5%):</td>
            <td>$finalCG</td>
            <td style="background-color:$overOrUnderColor">$overOrUnder</td>
          </tr>

        </table> 

    </div>
</div>


<!-- Submit and Reset button -->

<div align=center style=margin-top:10px>
    <form action="main.py">
        <input type="submit" value="Reset" />
    </form>
</div>


<div align=center style=margin-top:10px>
    <input type="submit" form="form1" value="Calculate">
</div>




</body>




<!-- Footer -->
<footer align=center style=margin-top:200px>
  <p>Created by A1C Geditz</p>
</footer>

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


