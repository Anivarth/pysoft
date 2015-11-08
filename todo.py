#hello world
import sqlite3
from bottle import route,run,debug,template,request,static_file

@route('/todo')
def todo_list():
	conn = sqlite3.connect('todo.db')
	c = conn.cursor()
	c.execute("SELECT id,task FROM todo WHERE status LIKE '1';")
	result = c.fetchall()
	c.close()
	output = template('make_table.tpl',rows=result)
	return output

@route('/new')
def new():
	return template('new_task.tpl')

@route('/new',method='POST')
def do_new():
	new = request.forms.get('task').strip();
	conn = sqlite3.connect('todo.db')
	c = conn.cursor()
	c.execute("INSERT INTO todo (task,status) VALUES (?,?);",(new,1))
	new_id = c.lastrowid
	conn.commit()
	c.close()
	return "The task was added successfully at %s"%new_id

@route('/css/style')
def style():
	return static_file('style.css',root='css/')


debug(True)
run(reloader=True)
