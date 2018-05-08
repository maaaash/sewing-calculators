from flask import Flask, render_template, request
app = Flask(__name__)

#homepage
@app.route("/")
def hello():
    return "Hello World!"
#calculators topic need to build the html page
@app.route("/calculators")
def calculators():
    return render_template("calculators.html")
#link for aline calculator
#link for skirt calculators

#aline skirt tutorial
@app.route("/calculators/aline")
def aline():
    return render_template("aline.html")
#ask for length of skirt, add some suggestions in html
#ask for width of waist
#ask for width of hips
#distance from waist to hips
if request.method == 'POST':
    length = float (request.form['length'])
    waist = float (request.form['waist'])
    hip = float (request.form['hip'])
    waist_hip_distance = float(request.form['waist_hip_distance'])

#put some way of calculating waist herE
#do I need something to return the number?
        return render_template("aline.html", pattern_waist=waist/2+1)
#unsure what this does
if __name__ == "__main__":
    app.run()
