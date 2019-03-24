# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 01:55:27 2019

@author: Nanda Krishna K S
"""

from flask import Flask, redirect, url_for, request, render_template
import Compute as mm
import numpy as np

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   word='Probability function of Random temperature is '+str(Prob_Calc(float(name)))
   print(word)
   return word

@app.route('/')
def FirstPage():
    return render_template('login.html', mean = round(mm.mean,2) ,median = round(mm.median,2), mode = round(mm.mode,2),
            var = round(mm.var,2), sd = round(mm.sd,2), rainy=round(mm.prob[0][0],2), sunny=round(mm.prob[0][1],2))

@app.route('/login',methods = ['POST', 'GET'])
def login():
   user = request.form['nm']
   if request.method == 'POST':
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

def Prob_Calc(rand_temp):
   prob_rand_temp=np.interp(float(rand_temp),mm.T,mm.power)
   return round(prob_rand_temp,1)

if __name__ == '__main__':
   app.run()
"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('hello.html',name = 'nanda')

if __name__ == '__main__':
   app.run(debug = True)
"""