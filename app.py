from flask import Flask, request, render_template
from services.call_service import make_outbound_call
from ivr_flows.level1 import level1_menu
from ivr_flows.level2 import level2_menu
from ivr_flows.action_handler import handle_action

app = Flask(__name__)


# Home page to enter destination number
@app.route("/")
def home():
    return render_template("index.html")


# Trigger outbound call
@app.route("/call", methods=["POST"])
def call():
    number = request.form["number"]
    return make_outbound_call(number)


# Level 1 IVR menu (language selection)
@app.route("/answer", methods=["GET", "POST"])
def answer():
    return level1_menu()


# Level 2 IVR menu (action selection)
@app.route("/level2", methods=["POST"])
def level2():
    return level2_menu()


# Final action (play audio or transfer)
@app.route("/action", methods=["POST", "GET"])
def action():
    return handle_action()


# Debug Endpoint
@app.route("/dial_status", methods=["POST"])
def dial_status():
    print("Calling")
    return "<Response></Response>"


if __name__ == "__main__":
    app.run(port=5000)
