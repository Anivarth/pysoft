<html>
<head>
	<title>Hello world</title>
	<link rel='stylesheet' href="css/style" />
</head>
%#template to generate a HTML table from a list of tuples(of lists of lists)
<p>The open items are as follows:</p>
<table>
	%for row in rows:
	<tr>
		%for col in row:
		<td>{{col}}</td>
		%end
	</tr>
	%end
</table>
</html>
