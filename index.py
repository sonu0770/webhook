from flask import Flask, request, abort,render_template
#curl -X POST -H "Content-Type: text/plain" --data "this is raw data" http://127.0.0.1:5000/webhook

app = Flask(__name__)


@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        print(str(request.data))
        with open('file.txt', 'a+') as data:
                data.write(str(request.data))
                data.write('\n')

        return 'success', 200

    elif request.method == 'GET':
            with open('wifi.txt', 'r') as f: 
                return render_template('index.html', text=f.read())
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
    #app.run(debug = False,host='0.0.0.0',port=5000)
