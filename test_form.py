#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
name=form.getvalue('name')
family=form.getvalue('family')
if name!=None or family!=None:
	print "Content-type:text/html"
	print 
	print "<br/>"
	print name, family

print"""Content-type:text/html

<form method-"post" action="form.py">
<textarea name="birthdate" cols="40" rows="5">
Your birthdate:
</textarea>
<textarea name="hobby" cols="40" rows="5">
Your hobby:
</textarea>
<br/>
<input type="submit" value="Submit">
</form>"""
