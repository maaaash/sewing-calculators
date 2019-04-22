from flask import Flask, render_template, request
app = Flask(__name__)

#homepage
@app.route("/")
def hello():
    return render_template("calculators.html")
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
#put some way of calculating waist here
@app.route("/calculators/alineresult", methods=['POST'])
def alineresult():
    length = float (request.form['length'])
    waist = float (request.form['waist'])
    hip = float (request.form['hip'])
    waist_hip_distance = float(request.form['waist_hip_distance'])
#hem calculation needs fixing
    return render_template("aline.html", pattern_waist = (waist+1)/2, pattern_waist_hip_distance = waist_hip_distance, pattern_hip = (hip+11)/2, pattern_hem = (waist)*1.17, pattern_half_hem = (waist/2)*1.8, pattern_length = length+3)


#do I need something to return the number?

#unsure what this does
if __name__ == "__main__":
    app.run()
