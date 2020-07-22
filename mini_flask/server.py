#!/usr/bin/env python

import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	data_path = os.environ["FILE"]
	with open(data_path, "r") as f:
		data = f.read()
	return data

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
