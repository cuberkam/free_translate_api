from http import HTTPStatus

from django.http import JsonResponse
from django.views import View
from googletrans import Translator
from googletrans.constants import LANGUAGES


class Translate(View):
    def get(self, request):
        translator = Translator()

        try:
            source_language = request.GET["sl"]
        except Exception:
            source_language = None

        try:
            destination_language = request.GET["dl"]
            text = request.GET["text"]
        except Exception:
            return JsonResponse(
                {"details": "dl or text fields are missing."},
                status=HTTPStatus.BAD_REQUEST,
            )

        if source_language is not None:
            translate_result = translator.translate(
                src=source_language, dest=destination_language, text=text
            )
        else:
            translate_result = translator.translate(
                dest=destination_language, text=text
            )

        response = build_response(translate_result)

        return JsonResponse(response)


def build_response(translate_result):
    source_language = translate_result.src
    source_text = translate_result.origin
    destination_language = translate_result.dest
    destination_text = translate_result.text

    phonetic = None
    try:
        phonetic = translate_result.extra_data["translation"][1][3]
    except Exception:
        phonetic = None

    source_text_audio = "https://translate.google.com/translate_tts?ie=UTF-&&client=tw-ob&tl={}&q={}".format(
        source_language, source_text
    )
    destination_text_audio = "https://translate.google.com/translate_tts?ie=UTF-&&client=tw-ob&tl={}&q={}".format(
        destination_language, destination_text
    )

    response = {
        "source-language": source_language,
        "source-text": source_text,
        "destination-language": destination_language,
        "destination-text": destination_text,
        "pronunciation": {
            "source-text-phonetic": phonetic,
            "source-text-audio": source_text_audio.replace(" ", "%20"),
            "destination-text-audio": destination_text_audio.replace(" ", "%20"),
        },
        "translations": build_translations(translate_result.extra_data),
        "definitions": build_definitions(translate_result.extra_data),
        "see-also": translate_result.extra_data["see-also"],
    }
    return response


def build_translations(extra_data):
    all_translations = []
    if extra_data["all-translations"] is not None:
        for item in extra_data["all-translations"][0][2]:
            all_translations.append(item[:2])
    else:
        all_translations = None

    possible_translations = []
    if extra_data["possible-translations"] is not None:
        for item in extra_data["possible-translations"][0][2]:
            possible_translations.append(item[0])
    else:
        possible_translations = None

    translations = {
        "all-translations": all_translations,
        "possible-translations": possible_translations,
        "possible-mistakes": extra_data["possible-mistakes"],
    }

    return translations


def build_definitions(extra_data):
    definitions = []
    part_of_speech = None
    definition = None
    example = None
    other_examples = None
    synonyms = None

    if extra_data["definitions"] is not None:
        for item in extra_data["definitions"]:
            part_of_speech = item[0]

            for in_item_1 in item[1]:
                g_id = in_item_1[1]
                definition = in_item_1[0]

                try:
                    example = in_item_1[2]
                except Exception:
                    example = None

                other_examples = built_examples(extra_data["examples"], g_id)

                synonyms = built_synonyms(extra_data["synonyms"], g_id)

                definitions.append(
                    {
                        "part-of-speech": part_of_speech,
                        "definition": definition,
                        "example": example,
                        "other-examples": other_examples,
                        "synonyms": synonyms,
                    }
                )
    else:
        definitions = None

    return definitions


def built_examples(examples, id):
    data = []

    if examples is not None:
        for item in examples:
            for in_item in item:
                if id == in_item[5]:
                    data.append(in_item[0])

        if data == []:
            return None

        return data

    else:
        return examples


def built_synonyms(synonyms, id):
    data = {}
    key = ""

    if synonyms is not None:
        for item in synonyms:
            for in_item in item[1]:
                if id == in_item[1]:
                    try:
                        key = in_item[2][0][0]
                    except Exception:
                        key = ""

                    data[key] = in_item[0]

        if data == {}:
            return None

        return data

    else:
        return synonyms


class Languages(View):
    def get(self, request):
        return JsonResponse(LANGUAGES)
