from flask import Flask, request, render_template, redirect, url_for
import os
import subprocess
#import test

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    # Save the user input to a file
    with open('user_input.txt', 'w') as f:
        f.write(user_input)
    # Run the Blender script
    #subprocess.run(['blender', '--background', '--python', 'create_model.py'])
    if user_input: subprocess.run(["python","test.py"])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
