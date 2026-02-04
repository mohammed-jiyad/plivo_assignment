from flask import Response, request
from config import BASE_URL


def level1_menu():
    digit = request.form.get("Digits")

    if digit in ["1", "2"]:
        xml = f"""
        <Response>
            <Redirect method="POST">{BASE_URL}/level2?lang={digit}</Redirect>
        </Response>
        """
        return Response(xml, mimetype="text/xml")

    xml = f"""
    <Response>
        <GetDigits action="{BASE_URL}/answer" method="POST" timeout="10" numDigits="1" retries="3">
            <Speak>Press 1 for English.</Speak>
            <Speak>Press 2 for Spanish.</Speak>
        </GetDigits>
        <Speak>No input received. Goodbye.</Speak>
    </Response>
    """
    return Response(xml, mimetype="text/xml")
