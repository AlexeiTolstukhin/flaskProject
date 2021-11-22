from flask import Flask, request, render_template
import db_functions

app = Flask(__name__)


@app.route('/')
def show_timetable_for_group():
    group = input()
    timetable = db_functions.get_timetable_by_group_title(group)
    return render_template(
        'timeTable.html',
        timetable=timetable
    )


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
