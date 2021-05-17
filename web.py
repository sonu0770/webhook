from flask import Flask, request, abort,render_template
from werkzeug.utils import secure_filename
#curl -X POST -H "Content-Type: text/plain" --data "this is raw data" http://127.0.0.1:5000/webhook

app = Flask(__name__)


@app.route('/webhook', methods=['POST','GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully',200
    else:
        abort(400)


if __name__ == '__main__':
    #app.run()
    app.run(debug = False,host='0.0.0.0',port=5000)