# streamlit project on gtts 
pip install ipython
pip install gtts
import  streamlit as st
from gtts import gTTS
st.set_page_config(page_title='Audio Message UI')
st.title('Audio Message ')
text_to_speech=gTTS('''birds of same feather flock together''')
text_to_speech.save('text_to_speech_gtts.wav')
sound_file='text_to_speech_gtts.wav'
Audio(sound_file,autoplay=False)


