from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
## thest
@app.route("/", methods=["GET"])
def index_get():
	return render_template("index.html")

@app.route("/", methods=["POST"])
def index_post():
	target_names = ["セトサ", "バージカラー", "バージニカ"]
	d = {
		"pl": request.form.get("pl"), 
		"pw": request.form.get("pw"), 
		"sl": request.form.get("sl"), 
		"sw": request.form.get("sw")
	}
	print(d.values())
	values = [float(v) for v in d.values()]
	print("values is", values)
	cls = joblib.load("svc.model")
	print("predict is", cls.predict([values]))
	d["pr"] = target_names[cls.predict([values])[0]]
	return render_template("index.html", **d)

if __name__ == "__main__":
	app.run(debug=True)
