#curl -X POST -H "Content-Type: text/plain" --data "this is raw data" http://127.0.0.1:5000/temp
from flask import Flask, request, abort,jsonify


app = Flask(__name__)


@app.route('/temp', methods=['POST'])
def temp():
	if request.method == 'POST':
		#data = request.data
		print(request.data)
		return 'success',200
	else:
		abort(400)


if __name__ == '__main__':
	app.run()