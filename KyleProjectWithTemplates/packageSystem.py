#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 15:56:02 2021

@author: kyledavis
"""

from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/statusUpdate")
def locationUpdate():
    return render_template("locationUpdate.html")

@app.route("/packageTracking")
def packageTracking():
    return render_template("packageTracking.html")

@app.route("/newPackage")
def newPackage():
    return render_template("newPackage.html")

if __name__ == "__main__":
    app.run(debug=True)