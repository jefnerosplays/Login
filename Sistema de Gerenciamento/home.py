from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    return render_template('Templates/login.html')
    username = request.form['username']
    password = request.form['password']
    if username == 'jeferson' and password == 'Jef#2023':
        return redirect (url_for('Templates\info.html'))
@app.route('/info')
def info():
    return render_template('Templates\info.html')