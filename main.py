from flask import Flask, render_template
import datetime

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def hello():
    return render_template('about.html', utc_dt=datetime.datetime.utcnow())

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)


if __name__=='__main__':
    app.run(debug = True)
