
import flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    # You can process the user input here as needed
    return redirect(url_for('display_video'))

@app.route('/display_video')
def display_video():
    video_path = 'C:/Users/HP/Documents/blender/output_animation.mp4'
    return render_template('display_video.html', video_path=video_path)

if __name__ == '__main__':
    app.run(debug=True)
