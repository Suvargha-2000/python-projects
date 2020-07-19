from bs4 import BeautifulSoup
from gtts import gTTS
from playsound import playsound
import requests
import speech_recognition as sr

def weather():


	r = sr.Recognizer()
	page =  requests.get('https://weather.com/en-IN/weather/tenday/l/65307c9954bbf461e71b8cb987691c0af427677700162d610cd37255f371240f')
	soup = BeautifulSoup(page.content , 'html.parser')
	kolkata = soup.find_all(class_ = "_-_-components-src-molecule-DaypartDetails-DailyContent-DailyContent--narrative--3Ti6_")


	cmnd = 'weather'

	lst_cmnd = ['today' , 'night' , 'tomorrow' , 'tomorrow_night']

	mic = sr.Microphone()

	night = kolkata[1].get_text()
	today = kolkata[0].get_text()
	tomorrow = kolkata[2].get_text()
	tomorrow_night = kolkata[3].get_text()




	with mic as source :
		print('listening')
		r.adjust_for_ambient_noise(source)
		comment = r.listen(source)

	command = r.recognize_google(comment)

	if cmnd in command:
		if lst_cmnd[0] in command:
			x=today
			y = 0
		if lst_cmnd[1] in command:
			x =night
			y =1

		if lst_cmnd[2] in command:
			x = tomorrow
			y = 2

		if lst_cmnd[3] in command:
			x = tomorrow_night
			y = 3



	for i in x :
		if i=='.' : 
			print("")
		else :
			print(i , end="")




	tts = gTTS(text=x, lang='en')
	tts.save("weather.mp3")

	spch = gTTS(text=('Nice to see you sir . '+lst_cmnd[y]+' weather is  '), lang='en')
	spch.save('welcome.mp3')

	playsound('welcome.mp3')
	playsound('weather.mp3')


