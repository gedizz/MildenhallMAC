#!C:\Users\Aegis\AppData\Local\Programs\Python\Python310\python.exe
import cgitb
from string import Template
cgitb.enable()

print("Content-Type: text/html;charset=utf-8")
print()  # <----------- additional newline for header/body separation.
# <meta http-equiv="refresh" content="60" >
# Below is the return to other parts of the website
print("Hello world")

html = """
<!DOCTYPE html>
<html>
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

</style>
<body>

<h2 align=center >Mildenhall %MAC Calculator</h2>

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
  
  
  <form id="form1"><input type="hidden" name="id" value="1" /></form>
  
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



</body>
</html>

"""
print(html)
