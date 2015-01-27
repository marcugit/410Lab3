#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
birthdate=form.getvalue('birthdate')
hobby=form.getvalue('hobby')
if birthdate!=None or hobby!=None:
	print "Content-type:text/html"
	print 
	print "<br/>"
	print birthdate, hobby

print """Content-type:text/html

<form method-"post" action="test_form.py">
<textarea name="name" cols="40" rows="5">
Your first name:
</textarea>
<textarea name="family" cols="40" rows="5">
Your last name:
</textarea>
<br/>
<input type="submit" value="Submit">
</form>"""



