from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def send_index():
    number = 0
    if request.method == 'POST':
        number = request.form.get('num')
    number = (int(number) ** 2) + (6 * int(number))
    return render_template('index.html', num=number)


app.run(debug=True)
