from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form method="POST" action="/">
            <label>Rotate by:</label>
                <input type="text" name="rot" value="0" />
            <input type="textarea" name="text" />
            <input type="submit" />
        </form>
    </body>
    </html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=["POST"])
def encrypt():
    rot = int(request.form['rot'])
    text = str(request.form['text'])
    encrypted_msg = ""
    for i in text:
        new_char = rotate_string(i, rot)
        encrypted_msg += new_char
    return "<h1>" + encrypted_msg + "</h1>"


app.run()