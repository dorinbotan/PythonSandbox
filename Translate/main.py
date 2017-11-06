from googleapiclient.discovery import build
import re


def main():
    file = open("tagarno_ko.ts", "r", encoding="utf8")
    text = file.read()
    file.close()

    source = re.findall('<source>(.*?)<\/source>', text)
    print(source)
    translation = []

    # Build a service object for interacting with the API.
    service = build('translate', 'v2', developerKey='AIzaSyBUu7AbrFKxkD7pU2nzJL1GMhRAPZnOcII')
    response = service.translations().list(
        source='en',
        target='ko',
        q=source[0:128]
        ).execute()
    translation += [v.get('translatedText') for v in response.get('translations')]

    response = service.translations().list(
        source='en',
        target='ko',
        q=source[128:256]
        ).execute()
    translation += [v.get('translatedText') for v in response.get('translations')]

    response = service.translations().list(
        source='en',
        target='ko',
        q=source[256:344]
        ).execute()
    translation += [v.get('translatedText') for v in response.get('translations')]

    print(len(source))
    print(len(translation))

    for i in range(100):
        match = source[i] + '<\/source>(|\n *)<translation>(.*?)<\/translation>'
        replace = source[i] + '</source>\n        <translation>' + translation[i] + '</translation>'
        text = re.sub(match, replace, text, 1)

    file = open("tagarno_ko.ts", "w", encoding="utf8")
    file.write(text)
    file.close()

if __name__ == '__main__':
    main()