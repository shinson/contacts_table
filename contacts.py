contacts = {'Aria': {'phone':'202-555-1234', 'twitter':'@montgomery', 'github':'@ezria'},
'Hanna':{'phone':'703-555-5678','twitter':'@marin', 'github':'@haleb'}, 'Spencer':{'phone':'646-555-4567',
'twitter':'@hastings', 'github':'@spoby'}, 'Emily':{'phone': '404-555-7890', 'twitter':'@fields',
'github':'@emilage'}}

# Goal 1: Loop through that dictionary to print out everyone's contact information.
# I used the items method for this one
for contact, info in sorted(contacts.items()):
	print "{0}'s contact information is:".format(contact)
	print "Phone: {0}".format(info['phone'])
	print "Twitter: {0}".format(info['twitter'])
	print "GitHub: {0}".format(info['github'])
	print " "
# Another option was to use the keys method
#for contact in sorted(contacts.keys()):
	#print "{0}'s contact information is:".format(contact)
	#print "Phone: {0}".format(contacts[contact]['phone'])
	#print "Twitter: {0}".format(contacts[contact]['twitter'])
	#print "GitHub: {0}".format(contacts[contact]['github'])
	#print " "
	
# Goal 2:  Display that information as an HTML table.
print '<table border="1">'
print '<tr>'
for contact, info in sorted(contacts.items()):
	print """<td colspan="3">{0}{1}\n{3}\n{2}\n{4}Phone: {5}{1}\n{4}Twitter: {6}{1}\n{4}Github: {7}{1}\n{3}""".format(contact, "</td>", "<tr>","</tr>","<td>",info['phone'], info['twitter'], info['github'])
	
print '</tr>'
print '</table>'

# Goal 3: Write all of the HTML out to a file called contacts.html and open it in your browser.
with open("contacts.html", "w") as contacts_file:
	contacts_file.write('<html>')
	contacts_file.write('\n<body>')
	contacts_file.write('\n<table border = "1">')
	
	for contact, info in sorted(contacts.items()):
		contacts_file.write("""\n{2}\n<td colspan="3">{0}{1}\n{3}\n{2}\n{4}Phone: {5}{1}\n{4}Twitter: {6}{1}\n{4}Github: {7}{1}\n{3}""".format(contact, "</td>", "<tr>","</tr>","<td>",info['phone'], info['twitter'], info['github']));
	
	contacts_file.write('\n</table>')
	contacts_file.write('\n</body>')
	contacts_file.write('\n</html>')

import webbrowser

webbrowser.open_new_tab("file:///Users/SoniaHinson/Documents/PythonClass/Shannon_Py_Ladies/Playtime/contacts.html")
 
contacts_file.close()
