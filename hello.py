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
    length = request.form['length']
    waist = request.form['waist']
    hip = request.form['hip']
    waist_hip_distance = request.form['waist_hip_distance']




#unsure what this does
if __name__ == "__main__":
    app.run()
