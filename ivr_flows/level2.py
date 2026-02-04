from flask import Response, request
from config import BASE_URL


def level2_menu():
    lang = request.args.get("lang", "1")  # default English

    if lang == "2":
        msg = """
        <Speak>Has seleccionado Español.</Speak>
        <Speak>Presione 1 para escuchar un mensaje.</Speak>
        <Speak>Presione 2 para hablar con un agente.</Speak>
        """
    else:
        msg = """
        <Speak>You selected English.</Speak>
        <Speak>Press 1 to hear a message.</Speak>
        <Speak>Press 2 to talk to an associate.</Speak>
        """

    xml = f"""
    <Response>
        <GetDigits action="{BASE_URL}/action?lang={lang}" method="POST" timeout="10" numDigits="1" retries="3">
            {msg}
        </GetDigits>
        <Speak>No valid input. Returning to main menu.</Speak>
        <Redirect method="POST">{BASE_URL}/answer</Redirect>
    </Response>
    """
    return Response(xml, mimetype="text/xml")
