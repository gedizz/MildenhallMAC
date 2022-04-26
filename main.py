#!C:\Users\Aegis\AppData\Local\Programs\Python\Python310\python.exe
import cgitb
import cgi
from string import Template


cgitb.enable()

print("Content-Type: text/html;charset=utf-8")
print()  # <----------- additional newline for header/body separation.
# <meta http-equiv="refresh" content="60" >
# Below is the return to other parts of the website
form = cgi.FieldStorage()
reserve1 = form.getvalue('1reserve')
print(reserve1)

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
    <td align=center><input form="form1" type="text" name="1reserve" value="" /></td>
    <td align=center><input form="form1" type="text" name="1main" value="" /></td>
    <td align=center><input form="form1" type="text" name="2main" value="" /></td>
    <td align=center><input form="form1" type="text" name="2main" value="" /></td>
    <td align=center><input form="form1" type="text" name="3main" value="" /></td>
    <td align=center><input form="form1" type="text" name="4main" value="" /></td>
    <td align=center><input form="form1" type="text" name="4reserve" value="" /></td>
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
    <td align=center><input form="form1" type="text" name="aft" value="" /></td>
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
    <td align=center><input form="form1" type="text" name="upper" value="" /></td>
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
print(html)

