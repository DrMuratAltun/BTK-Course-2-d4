#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def filetospeech(file_path,lang_input='tr',slow=False):
    from gtts import gTTS
    metin=''
    try:
        with open (file_path,'r',encoding='utf-8') as file:
            for line in file:
                metin+=line
        print(metin)
        kayit=gTTS(text=metin,lang='tr',slow=False)
        dosya_adi=str(metin[:5])
        dosya_adi+='.mp3'
        kayit.save(dosya_adi)
        print('Ses kaydedildi.:',dosya_adi)
    except:
        print('Ses kaydedilemedi.')

