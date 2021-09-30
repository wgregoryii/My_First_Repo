from flask import Flask


app = Flask(__name__)

#Web Path
@app.route("/")
def stevie():
    return "Hello World!"

#Web Path
@app.route("/second")
def second():
    return "This is the second page"

@app.route('/third/subthird')
def seconds():
    return "This is a sub page of Page 2"

@app.route("/forth/<string:id>")
def forth(id):
    return f"ID of this page is {id}"

if __name__=="__main__":
    app.run(host='0.0.0.0', port=80)
    # app.run(debug=True)