from flask import Response, request
from config import ASSOCIATE_NUMBER, BASE_URL, SOURCE_NUMBER
from utils.helpers import is_same_number


def handle_action():
    digit = request.form.get("Digits")
    lang = request.args.get("lang", "1")
    caller_number = request.form.get("From")

    # Default response safeguard
    xml = "<Response><Speak>Invalid option. Goodbye.</Speak></Response>"

    if digit == "1":
        if lang == "2":
            speech = "<Speak>Reproduciendo su mensaje.</Speak>"
        else:
            speech = "<Speak>Playing your message.</Speak>"

        xml = f"""
        <Response>
            {speech}
            <Play>https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3</Play>
        </Response>
        """

    elif digit == "2":
        if is_same_number(caller_number, ASSOCIATE_NUMBER):
            xml = """
            <Response>
                <Speak>You are already connected to this number. Transfer not possible.</Speak>
            </Response>
            """
        else:
            xml = f"""
            <Response>
                <Speak>Connecting you to an associate.</Speak>
                <Dial action="{BASE_URL}/dial_status" method="POST" callerId="{SOURCE_NUMBER}">
                    <Number>{ASSOCIATE_NUMBER}</Number>
                </Dial>
            </Response>
            """

    return Response(xml, mimetype="text/xml")
