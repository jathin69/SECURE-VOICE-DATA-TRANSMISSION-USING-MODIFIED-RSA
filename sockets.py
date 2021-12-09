import socket
s=socket.socket()
import speech_recognition as sr
import RSA_cryptoproj  as cry
import HashingAndSalting as hs
import hashlib
port=1234
ip="192.168.43.254"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        print("You said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    text=r.recognize_google(audio)
    print(text)
    enc=cry.encrypt_string(text)
    encrypted_salted_text = hs.salt(enc)
    print(encrypted_salted_text)
#hashing done through SHA-256 algorithm
    Sender_HASH = hashlib.sha256(encrypted_salted_text.encode()).hexdigest()
    client.send(enc.encode())
    print(enc)
    client.send(Sender_HASH.encode())
