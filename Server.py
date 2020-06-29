from flask import Flask, render_template, url_for, request,redirect
import csv
app = Flask(__name__)
print(__name__)

# @app.route('/')
# def hello_world():
# 	return render_template('index.html')


@app.route('/')
def my_home():
	return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)


# def write_to_dbfile(data):
# 	with open('database.txt', 'a') as dbfile:
# 		email = data['email']
# 		subject = data['subject']
# 		message = data['message']
# 		file = dbfile.write(f'\n {email}, {subject}, {message}')


def write_to_csv(data):
	with open('db.csv', newline='', mode='a') as dbcsv:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csvwriter = csv.writer(dbcsv, delimiter=',', quotechar='"' , quoting=csv.QUOTE_MINIMAL)
		csvwriter.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return redirect('/thankyou.html')
	else:
		return 'something went wrong. Try again!'



