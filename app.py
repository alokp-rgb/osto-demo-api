import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/run")
def run():
    cmd = request.args.get("cmd")
    return subprocess.check_output(cmd, shell=True)


@app.route("/user")
def user():
    uid = request.args.get("id")
    conn = sqlite3.connect("app.db")
    return str(conn.execute("SELECT * FROM users WHERE id = " + uid).fetchall())


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
