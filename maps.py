from flask import Flask, render_template, abort

app = Flask(__name__)


class School:
    def __init__(self, key, name, lat, lng):
        self.key = key
        self.name = name
        self.lat = lat
        self.lng = lng


schools = (
    School('sm', 'Samara', 53.2001, 50.15),
    School('ms', 'Moscow', 55.7522, 37.6156),
    School('sp', 'Saint-Petersburg', 59.9386, 30.3141),
    School('or', 'Orenburg', 51.7727, 55.0988),
    School('nv', 'Nizhny Novgorod', 56.3287, 44.002)
)
schools_by_key = {school.key: school for school in schools}


@app.route("/")
def index():
    return render_template('index.html', schools=schools)


@app.route("/<school_code>")
def show_school(school_code):
    school = schools_by_key.get(school_code)
    if school:
        return render_template('map.html', school=school)
    else:
        abort(404)


if __name__ == "__main__":
    app.run(host='localhost', debug=True)
