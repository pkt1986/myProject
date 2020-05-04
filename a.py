import pyttsx3 as t

engine = t.init()
# v = engine.getProperty('voices')
# print(len(v))
# for i in v:
#     print('-'*60)
#     print(i.name, i.languages, i.gender, i.age)
#     print('*'*60)
engine.say("aahhh  fuckyou         man")
engine.runAndWait()
