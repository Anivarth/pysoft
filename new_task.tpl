<html>
<head>
	<title>Hello world</title>
	<link rel='stylesheet' href="css/style" />
</head>
<p>Add a new task to the ToDo list:</p>
<form action="/new" method="POST">
	<input type="text" size="100" maxlength="100" name="task">
	<input type="submit" name="save" value="save">
</form>
</html>
