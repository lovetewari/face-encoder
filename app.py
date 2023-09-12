from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_recognition', methods=['GET', 'POST'])
def start_recognition():
    # Integrate your existing script here to start the recognition process
    # ...
    return jsonify(status="success")

if __name__ == '__main__':
    app.run(debug=True)
