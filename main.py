# بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ  ﷺ
# InshaAllah, By his marcy I will Gain Success

from flask import Flask
from flask import render_template,send_file

app = Flask(__name__)

@app.get('/')
def root():
 return render_template('index.html')


@app.get('/projects')
def projects():
 return render_template('projects.html')




if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=4000 ,debug=True)