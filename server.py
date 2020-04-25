from flask import Flask ,render_template, url_for,  request , redirect
app=Flask(__name__)

@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/index.html')
def my_home1():
	return render_template('index.html')

@app.route('/<string:page_name>')
def htmlpage(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt' , mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email},{subject},{message}')




@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
	if request.method== 'POST':
		data=request.form.to_dict()
		write_to_file(data)
		return redirect('/thankyou.html')
	else :
		return 'Something went Wrong, Try Again'