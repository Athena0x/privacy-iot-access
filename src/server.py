from flask import Flask, request, jsonify
from access_control import AccessControl

app = Flask(__name__)
ac = AccessControl()
ac.assign_role("device_1", "sensor_data")

@app.route("/auth", methods=["POST"])
def auth():
    data = request.json
    user, resource = data["user"], data["resource"]
    return jsonify({"access": ac.has_access(user, resource)})

if __name__ == "__main__":
    app.run(port=5000)
