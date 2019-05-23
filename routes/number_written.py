from flask import jsonify, Blueprint


TECHNICAL_CHALLENGE_API = Blueprint('number_written', __name__)


def get_blueprint():
    return TECHNICAL_CHALLENGE_API


@TECHNICAL_CHALLENGE_API.route('/<path:number>', methods=['GET'])
def number_written(number):
    """
    Get the number written
    @param number: the number
    @return: 200: a number written as a flask/response object with application/json mimetype.
    """
    import inflect
    from googletrans import Translator

    inflect_engine = inflect.engine()

    start, end = -99999, 99999
    for index in range(start, end + 1):
        if not number.replace('-', '').isdigit():
            return jsonify(success=f"Invalid characters '{number}'"), 404

        if index == int(number):
            words_in_english = inflect_engine.number_to_words(int(number))

            transalator = Translator()
            translated_words = transalator.translate(text=words_in_english, dest='pt')
            translated_words_text = translated_words.text
            if translated_words_text.isdigit():
                translated_words_text = translated_words.extra_data['all-translations'][0][1][0]

            return jsonify({"extenso": translated_words_text})
    return jsonify(success=f"Invalid number '{number}'"), 404
