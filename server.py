from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = 'reallytiredofsecrets'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template("ninja.html")

@app.route('/ninja/<color>', methods = ['GET'])
def ninja_color(color):
	if color == 'red':
		return render_template("/ninja.html", color = red)
		flash('It's Raphael')
	elif color == 'blue':
		return render_template("/ninja.html", color = blue)
		flash('It's Leonardo')
	elif color == 'purple':
		return render_template("/ninja.html", color = purple)
		flash('It's Donatello')
	elif color == 'orange':
		return render_template("/ninja.html", color = orange)
		flash('It's Michelangelo')
	else:
    return render_template("/ninja.html")
    	flash('It's Megan Foxx')

app.run(debug=True)
