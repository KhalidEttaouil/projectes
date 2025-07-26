# import pydub
# import vonage
# from pydub import AudioSegment
# from pydub.playback import play
# import datetime
# helo = AudioSegment.from_wav("sound/1.wav")
# play(helo)
# time = input('Enter time you wanna eat medcine like 00:00:00 :').strip()
# oki = AudioSegment.from_wav("sound/2.wav")
# play(oki)
# while True:
#     timo = datetime.datetime.now()
#     now = timo.strftime('%H:%M:%S')
#     if now == time:
#         medcine = AudioSegment.from_wav("sound/3.wav")
#         play(medcine)
#         client = vonage.Client(key="0b2c6ce0", secret="SAysMCQnxx4RDVEh")
#         sms = vonage.Sms(client)
#         responseData = sms.send_message(
#     {
#         "from": "KHALDRIC",
#         "to": "212780602947",
#         "text": "WSALAT LW9AYTA DYAL DWAK MATNSACH TA5DO O LAH ICHAFIK",
#     }
# )

#     if responseData["messages"][0]["status"] == "0":
#           print("Message sent successfully.")
#     else:
#           print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
#     if now > time:
#         later = AudioSegment.from_wav("sound/4.wav")
#         play(later)
#         break
   # py -3.11 medcine.py
# import pydub
# from pydub import AudioSegment
# from pydub.playback import play
# import vonage
# import datetime
# import time  # لإضافة sleep

# # تشغيل الصوت الأول
# helo = AudioSegment.from_wav("sound/1.wav")
# play(helo)

# # إدخال الوقت
# target_time = input('⏰ Enter time to take medicine (like 14:30:00): ').strip()

# # تشغيل الصوت الثاني بعد الإدخال
# oki = AudioSegment.from_wav("sound/2.wav")
# play(oki)

# # بدأ المراقبة
# while True:
#     now = datetime.datetime.now().strftime('%H:%M:%S')

#     if now == target_time:
#         # تشغيل صوت الدواء
#         medcine = AudioSegment.from_wav("sound/3.wav")
#         play(medcine)

#         # إرسال رسالة SMS عبر Vonage
#         client = vonage.Client(key="0b2c6ce0", secret="SAysMCQnxx4RDVEh")
#         sms = vonage.Sms(client)

#         responseData = sms.send_message({
#             "from": "KHALDRIC",
#             "to": "212780602947",
#             "text": "🚨 WSALAT LW9AYTA DYAL DWAK, MATNSACH TA5DO. ALLAH ISHAFIK 🤲"
#         })

#         if responseData["messages"][0]["status"] == "0":
#             print("✅ Message sent successfully.")
#         else:
#             print(f"❌ Message failed: {responseData['messages'][0]['error-text']}")

#         # تشغيل صوت بعد الإرسال
#         later = AudioSegment.from_wav("sound/4.wav")
#         play(later)
#         break

#     # ننتظر 1 ثانية
#     time.sleep(1)
import vonage
print("Vonage موجود؟", hasattr(vonage, "Client"))  # يجب أن يعطي True
