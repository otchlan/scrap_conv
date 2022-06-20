from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')
#todo do tego trzeba będzie stworzyć plik .env -
# app.config['SECRET_KEY'] = session_sec_key

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=5000)