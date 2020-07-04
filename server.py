from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)


@app.route('/')
def a_whole_new_world():
	return render_template("index.html")

@app.route('/index.html')
def home():
	return render_template("index.html")

@app.route('/works.html')
def works():
	return render_template("works.html")


@app.route('/about.html')
def about():
	return render_template("about.html")

@app.route('/contact.html')
def contact():
	return render_template("contact.html")


@app.route('/<page_name>')
def auto_html_page(page_name):
	return render_template(page_name)

# @app.route('/components.html')           #Alternative Below!
# def components():
#     return render_template('components.html')


# def dynamics(words):                     #This can be used but below is a better way (But this was made by me, Cheers!!)
# 	link = '/' + words + '.html' 
# 	@app.route(link)
# 	def route():
# 		html_page = words + '.html'
# 		return render_template(html_page)

# dynamics('components')

def write_to_file(data):
	with open('database.txt', mode = 'a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		print(email)
		file = database.write(f'\n\n {email} \n {subject} \n {message} \n')

def write_to_csv(data):
	with open('database.csv', mode = 'a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		print(email)
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])


# @app.route('/submit_form', methods=['POST','GET'])
# def form_submit_txt():
# 	if request.method == 'POST':
# 		info = request.form.to_dict()
# 		print(info)
# 		write_to_file(info)

# 		return redirect('/thank_you.html')
# 	else:
# 		return 'something went wrong'                           

@app.route('/submit_form', methods=['POST','GET'])
def form_submit_csv():
	if request.method == 'POST':
		info = request.form.to_dict()
		print(info)
		write_to_csv(info)

		return redirect('/thank_you.html')
	else:
		return 'something went wrong'                           
