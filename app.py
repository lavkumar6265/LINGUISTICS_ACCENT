from gtts import gTTS
import gradio as gr
# from googletrans import Translator
import mtranslate

lang = {'Afrikaans': 'af','Arabic':'ar','Bulgarian':'bg','Bengali':'bn','Bosnian':'bs',
'Catalan':'ca','Czech':'cs','Danish':'da','German':'de','Greek':'el','English':'en',
'Spanish':'es','Estonian':'et','Finnish':'fi','French':'fr','Gujarati':'gu','Hindi':'hi',
'Croatian':'hr','Hungarian':'hu','Indonesian':'id','Icelandic':'is','Italian':'it',
'Hebrew':'iw','Japanese':'ja','Javanese':'jw','Khmer':'km','Kannada':'kn','Korean':'ko',
'Latin':'la','Latvian':'lv','Malayalam':'ml','Marathi':'mr','Malay':'ms',
'Myanmar (Burmese)':'my','Nepali':'ne', 'Dutch':'nl','Norwegian':'no',
'Polish':'pl','Portuguese':'pt','Romanian':'ro','Russian':'ru','Sinhala':'si',
'Slovak':'sk', 'Albanian':'sq','Serbian':'sr','Sundanese':'su','Swedish':'sv',
'Swahili':'sw','Tamil':'ta','Telugu':'te','Thai':'th','Filipino':'tl','Turkish':'tr',
'Ukrainian':'uk','Urdu':'ur','Vietnamese':'vi','Chinese (Simplified)':'zh-CN',
'Chinese (Mandarin/Taiwan)':'zh-TW',
'Chinese (Mandarin)':'zh'}

tld = {'English(Australia)':'com.au', 'English (United Kingdom)':'co.uk',
'English (United States)':'us', 'English (Canada)':'ca','English (India)':'co.in',
'English (Ireland)':'ie','English (South Africa)':'co.za','French (Canada)':'ca',
'French (France)':'fr','Portuguese (Brazil)':'com.br','Portuguese (Portugal)':'pt',
'Spanish (Mexico)':'com.mx','Spanish (Spain)':'es','Spanish (United States)':'us'}

# def T2TConversion(sentence, language):
#     translator = Translator()
#     translation = translator.translate(sentence, dest = lang[language])
#     return translation.text


def T2TConversion(sentence, language):
    translated_text = mtranslate.translate(sentence, lang[language])
    return translated_text


def convert_text(Text, Accent):
    """ Performs Text-To-Speech provided language and accent.] """
    
    tts = gTTS(Text, tld[Accent])
    tts.save('tts.mp3')
    with open('tts.mp3') as fp:
        return fp.name
  
   
def start():
    it_1 = gr.Interface(fn = convert_text, 
        inputs = [
            gr.TextArea(label = 'The Text to be Converted to Audio'),
            gr.Dropdown([key for key,_ in tld.items()])],
        outputs = gr.Audio(),
        title = 'A Text-To-Speech Converter for Low Resource Languages',
        description=  'Support over 50 languages !',
        article= 'How does it work ? Just write a sentence (in target language) in the space provided and select the accent and press submit. That is it. Wait and Enjoy.')
        
    it_2 =  gr.Interface(fn=T2TConversion, 
        inputs = [ 
            gr.Text(label='Write a sentence in English'),
            gr.Dropdown([key for key,_ in lang.items()])], 
        outputs= gr.Text(label='The Converted Text'),
        title = 'Translation from English',
        description='Write a sentence in english and convert to other languages for speech synthesis',
        article='What if you do not have a sentence in a particular language? Just write the sentence in english and let us do the magic.')

    demo = gr.TabbedInterface([it_1,it_2],['Speech Synthesis', 'Sentence Translation'])
    demo.launch()

start()