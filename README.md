# Free Translate API

## ⚠️ Important Notice

The website hosted on PythonAnywhere is for demonstration purposes only. This is not a public API service and does not support external API hosting.

If you want to use this project as an API, please clone the repository and host it on your own server or cloud platform.

## 📖 Usage Guide

With the Free Translate API, you can translate words or sentences into the language you want. There are 2 ways to do this.

**URL Parameters**

- sl = Source language code
- dl = Destination language code
- text = word or sentence

**First Way:** By querying with sl, dl and text parameters.

**Second Way:** By querying with dl and text parameters. The language of the text parameter is automatically detected.

> Use the `/languages` endpoint to see which languages are supported.

`/translate?sl=en&dl=tr&text=example` or `/translate?dl=tr&text=example`
```json
{
  "source-language": "en",
  "source-text": "example\n",
  "destination-language": "tr",
  "destination-text": "örnek",
  "pronunciation": {
    "source-text-phonetic": "iɡˈzampəl",
    "source-text-audio": "https://translate.google.com/translate_tts?ie=UTF-&&client=tw-ob&tl=en&q=example\n",
    "destination-text-audio": "https://translate.google.com/translate_tts?ie=UTF-&&client=tw-ob&tl=tr&q=örnek"
  },
  "translations": {
    "all-translations": [
      [
        "örnek",
        [
          "example",
          "sample",
          "instance",
          "model",
          "specimen",
          "pattern"
        ]
      ],
      [
        "misal",
        [
          "example",
          "instance"
        ]
      ],
      [
        "ibret",
        [
          "lesson",
          "example",
          "warning",
          "object lesson",
          "one in the eye"
        ]
      ],
      [
        "ders",
        [
          "lesson",
          "class",
          "lecture",
          "teaching",
          "subject",
          "example"
        ]
      ]
    ],
    "possible-translations": [
      "örnek",
      "örnek vermek",
      "misal",
      "mesela",
      "örneğin"
    ],
    "possible-mistakes": null
  },
  "definitions": [
    {
      "part-of-speech": "isim",
      "definition": "a thing characteristic of its kind or illustrating a general rule.",
      "example": "it's a good example of how European action can produce results",
      "other-examples": [
        "it's a good <b>example</b> of how European action can produce results"
      ],
      "synonyms": {
        "": [
          "specimen",
          "sample",
          "exemplar",
          "exemplification",
          "instance",
          "case",
          "representative case",
          "typical case",
          "case in point",
          "illustration"
        ]
      }
    },
    {
      "part-of-speech": "isim",
      "definition": "a person or thing regarded in terms of their fitness to be imitated or the likelihood of their being imitated.",
      "example": "it is vitally important that parents should set an example",
      "other-examples": [
        "it is vitally important that parents should set an <b>example</b>",
        "she followed her brother's <b>example</b> and deserted her family"
      ],
      "synonyms": {
        "": [
          "precedent",
          "lead",
          "guide",
          "model",
          "pattern",
          "blueprint",
          "template",
          "paradigm",
          "exemplar",
          "ideal",
          "standard",
          "parallel case",
          "role model"
        ]
      }
    },
    {
      "part-of-speech": "fiil",
      "definition": "be illustrated or exemplified.",
      "example": "the extent of Allied naval support is exampled by the navigational specialists provided",
      "other-examples": null,
      "synonyms": null
    }
  ],
  "see-also": null
}
```

`/translate?sl=en&dl=tr&text=hello%20world` or `/translate?dl=tr&text=hello%20world`
```json
{
  "source-language": "en",
  "source-text": "hello world",
  "destination-language": "tr",
  "destination-text": "Selam Dünya",
  "pronunciation": {
    "source-text-phonetic": null,
    "source-text-audio": "https://translate.google.com/translate_tts?ie=UTF-&&client=tw-ob&tl=en&q=hello%20world",
    "destination-text-audio": "https://translate.google.com/translate_tts?ie=UTF-&&client=tw-ob&tl=tr&q=Selam%20Dünya"
  },
  "translations": {
    "all-translations": null,
    "possible-translations": [
      "Selam Dünya",
      "merhaba dünya"
    ],
    "possible-mistakes": null
  },
  "definitions": null,
  "see-also": null
}

```
