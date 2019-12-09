from flask import Flask, render_template

from InputSaver import InputSaver

app = Flask(__name__)


@app.route('/')
def show_task():
    return render_template("task.html")


@app.route('/', methods=['POST'])
def save_input():
    return InputSaver().save_data()


if __name__ == '__main__':
    app.run(port=8090)
