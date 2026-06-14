from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["audio"]

    file.save("uploads/" + file.filename)

    return jsonify({
        "message":"Đã nhận file!"
    })

app.run(debug=True)