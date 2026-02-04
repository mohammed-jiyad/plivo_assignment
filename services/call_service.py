import plivo
from config import AUTH_ID, AUTH_TOKEN, SOURCE_NUMBER, BASE_URL

client = plivo.RestClient(AUTH_ID, AUTH_TOKEN)


def make_outbound_call(number):

    if not number.startswith("+"):
        return "Invalid phone number format. Use +countrycode."

    try:
        response = client.calls.create(
            from_=SOURCE_NUMBER,
            to_=number,
            answer_url=f"{BASE_URL}/answer",
            answer_method="POST",
        )

        # FIXED LINE
        return f"Call Started Successfully! ID: {response.request_uuid}"

    except Exception as e:
        return f"Call failed: {str(e)}"
