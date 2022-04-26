#!C:\Users\Aegis\AppData\Local\Programs\Python\Python310\python.exe
import cgitb
import cgi
from string import Template
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
    "aftbody": form.getvalue("aftbody"),
    "upperdeck": form.getvalue("upperdeck"),
    "main3": form.getvalue("3main"),
    "main4": form.getvalue("4main"),
    "reserve4": form.getvalue("4reserve")
}
# If no data is received (likely first going to site) then set all values to 0 so we dont accidentally get NoneType
for x in data:
    if data[x] == None:
        data[x] = "0"

# reserve1 = form.getvalue('1reserve')
# main1 = form.getvalue('1main')
# main2 = form.getvalue('2main')
# forwardBody = form.getvalue('forwardbody')
# aftBody = form.getvalue('aftbody')
# upperDeck = form.getvalue('upperdeck')
# main3 = form.getvalue('3main')
# main4 = form.getvalue('4main')
# reserve4 = form.getvalue('4reserve')




# Below is all HTML
html = """
<!DOCTYPE html>
<html>

<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>

table, th {
  border:1px solid black;

}

.special {
border:0px;
}

td {
  width: 14.2%;
  border:1px solid black;
  
}

input {
margin-top: 5px;
margin-bottom: 5px;
}

footer {
width:100%;
}


</style>
<body>

<h2 align=center >Mildenhall %MAC Calculator</h2>




<!-- Main Table -->
<table style="width:100%">

  <tr style="background-color:#ADADAA">
    <th>#1 Reserve</th>
    <th>#1 Main</th>
    <th>#2 Main</th>
    <th>Forward Body</th>
    <th>#3 Main</th>
    <th>#4 Main</th>
    <th>#4 Reserve</th>
  </tr>
  
  
  <form action="main.py" id="form1"><input type="hidden" name="id" value="1" method="get"/></form>
  
  <tr>
    <td align=center><input form="form1" type="text" name="1reserve" value="$r1" /></td>
    <td align=center><input form="form1" type="text" name="1main" value="$m1" /></td>
    <td align=center><input form="form1" type="text" name="2main" value="$m2" /></td>
    <td align=center><input form="form1" type="text" name="forwardbody" value="$fwd" /></td>
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


<!-- Submit button -->
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

html_replaced = Template(html).safe_substitute(
    r1="{data[reserve1]}",
    m1="{data[main1]}",
    m2="{data[main2]}",
    fwd="{data[forwardBody]}",
    aft="{data[aftBody]}",
    up="{data[upperDeck]}",
    m3="{data[main3]}",
    m4="{data[main4]}",
    r4="%s" % (data["reserve4"]))
print(html_replaced)

# print(html)

