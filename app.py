from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return "hello world"

if __name__ == '__main__':
   app.run(debug = True)

def function():
	return render_template(
		"index.html")
