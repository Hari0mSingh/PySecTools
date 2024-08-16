# The provided script demonstrates how to use the mechanize library in Python to interact with a web form programmatically

import mechanizepip

# Creating a browser object
br = mechanize.Browser()

# Opening a website
br.open('http://example.com')

# Selecting and filling out a form
br.select_form(nr=0)
br.form['username'] = 'user'
br.form['password'] = 'pass'
br.submit()
