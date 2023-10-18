from flask import Flask, render_template ,request
import time
import smtplib
import os
import re
from pdf2image import convert_from_bytes
import cProfile


app = Flask(__name__)

def mail(email, pssd, mssg):
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, pssd)
    server.sendmail(email, 'metanalyzer@gmail.com', mssg)

    server.quit()




@app.route('/')
def home_page():
    return render_template("index.html")


def cleanMsg(data):
    name= data.get('name')
    email= data.get('email')
    msg=data.get('message')
    message = f"""From: {name} <{email}>
Subject: New Message On Our Official Website
{msg}
"""
    return message

@app.route('/submit_form',methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        data = request.form.to_dict()
        msg=cleanMsg(data)
        password=os.environ.get('EMAIL_PASS')
        mail('metanalyzer@gmail.com', password, msg)
        return render_template("index.html",code="improve_indexes()")
    else:
        return f"Something Not Right "
    

@app.errorhandler(404)  
def not_found(e): 
  return render_template("404.html")



if __name__ == '__main__':
    app.run(debug=True)
