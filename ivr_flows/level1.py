from flask import Response, request
from config import BASE_URL


def level1_menu():
    digit = request.form.get("Digits")
    retry = int(request.args.get("retry", 0))  # Track retry count

    # Correct input
    if digit in ["1", "2"]:
        xml = f"""
        <Response>
            <Redirect method="POST">{BASE_URL}/level2?lang={digit}</Redirect>
        </Response>
        """
        return Response(xml, mimetype="text/xml")

    # If wrong input OR no input
    if retry >= 2:
        xml = """
        <Response>
            <Speak>Invalid input received multiple times. Goodbye.</Speak>
        </Response>
        """
        return Response(xml, mimetype="text/xml")

    # Ask again
    xml = f"""
    <Response>
        <Speak>Invalid or no input.</Speak>
        <GetDigits action="{BASE_URL}/answer?retry={retry+1}" 
                   method="POST" timeout="10" numDigits="1">
            <Speak>Press 1 for English.</Speak>
            <Speak>Press 2 for Spanish.</Speak>
        </GetDigits>
        <Speak>No input received. Goodbye.</Speak>
    </Response>
    """
    return Response(xml, mimetype="text/xml")
