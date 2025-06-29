from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

def extract_video_id(url):
    # Regular expression to capture different YouTube URL formats
    video_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
    if video_id_match:
        return video_id_match.group(1)
    return None

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        video_url = request.form['video_url']
        video_id = extract_video_id(video_url)
        if video_id:
            return redirect(url_for('home', video_id=video_id))
        else:
            return redirect(url_for('home'))
    
    video_id = request.args.get('video_id', 'M7lc1UVf-VE')
    return render_template('index.html', video_id=video_id)

if __name__ == '__main__':
    app.run(debug=True)
