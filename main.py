from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def send_index():
    number = 0
    new_name = '???'
    if request.method == 'POST':
        number = request.form.get('num')
        new_name = request.form.get('name')
    number = (int(number) ** 2) + (6 * int(number))
    return render_template('index.html', num=number, name=new_name)


app.run(debug=True)
