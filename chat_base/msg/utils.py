# utils.py
from deep_translator import GoogleTranslator
'''
def translateLang(messages, target_language):
    for msg in messages:
        if target_language != 'en':
            try:
                msg.translated_text = GoogleTranslator(source='auto', target=target_language).translate(msg.text)
            except Exception as e:
                msg.translated_text = msg.text  # fallback
        else:
            msg.translated_text = msg.text
    return messages
'''

def translateLang(msg,lang):
    try:
        msg = GoogleTranslator(source='auto', target=lang).translate(msg)
    except Exception as e:
        pass
    return msg
