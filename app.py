from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Экзамен ВИС 602'
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)