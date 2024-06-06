from WPP_Whatsapp import Create
from django.conf import settings
import time
from concurrent import futures
import sys
from . import views
# from playwright._impl import _api_types 
# if __name__ == '__main__':
    # from .views import catchgenqr
# import psutil

# genqr = ""

    # openWhatsapp()


def catchqr(qrCode: str , asciiQR: str , attempt: int, urlCode: str):
            """
            qrCode:"data:image/png;base64,",
            asciiQR:"",
            attempt:1,
            urlCode:"2@242",
            """
            
            getqr = asciiQR
            print(getqr)
            
            # global genqr
            genqr =qrCode
            # test = testqr()
            # print(test)
            # print(asciiQR)
            # print(attempt)
            # print(urlCode)

creator = ""
client = ""
# wpIsConnected = False
class openWhatsapp():
        # start client with your session name
    client = None
    creator = None
    @classmethod
    def wp(cls):
    
        # from .views import catchgenqr
        your_session_name = "clinical" #"test"
        # global creator
        cls.creator = Create(session=your_session_name, catchQR= views.catchgenqr , logQR= True) #catchgenqr
        settings.GLOBAL_VAR = creator
        settings.WP_IS_CONNECTED = False
        # try:
        cls.client = cls.creator.start()
        # if client.waitForLogin():
        #     time.sleep(10) 
        # except futures._base.TimeoutError():
        #     time.sleep(7)
        #     client.close()
    # Now scan Whatsapp Qrcode in browser
    # check state of login
        if cls.creator.state != 'CONNECTED':
            
            raise Exception(cls.creator.state)
        if cls.creator.state == 'CONNECTED' : #and (creator.session == DocName):

            settings.WP_IS_CONNECTED = True
        
        # time.sleep(5)
    @classmethod
    def closewp(cls):
        # openWhatsapp.client.close()
        cls.client.close()
    

def whatsappApi(patientName, doctorName, whatsappNumber, time_, date, clinicName):
    # reclient= openWhatsapp.client
    # from .views import catchgenqr
    phone_number = f"+91{whatsappNumber}" #phone_number = "+917904427507"  # or "+201016708170"
    message = f"APPOINTMENT REMINDER: Dear {patientName}, This is Dr.{doctorName}, from {clinicName}. You have an appointment in three hours. Your Appointment is fixed at {time_} on {date}."
    
    # Sesscreator = Create(session=doctorName, catchQR= catchgenqr, logQR= True)
    # sess = Sesscreator.session
    # global client
    # try:
    #     sessStart = Sesscreator.start()
    #     if sessStart.waitForLogin():
    #         time.sleep(10)
    # except futures._base.TimeoutError():
    #     result = sessStart.sendText(phone_number, message)
    #     sessStart.close()    
    # dumSess = sessStart.session
    result = openWhatsapp.client.sendText(phone_number, message)
    # time.sleep(5)
    # sessStart.close()
    
        
def whatsappApiDoc(doctorName, whatsappNumber, time_, date, patientName, patientNumber):
    # from .views import catchgenqr
    phone_number = f"+91{whatsappNumber}" #phone_number = "+917904427507"  # or "+201016708170"
    message = f"APPOINTMENT REMINDER: Dear {doctorName}, You have an appointment in three hours, fixed at {time_} on {date}, with {patientName}. Patient Mobile No: {patientNumber} Thanks!!"
    # global client
    # # Simple message
    # result = client.sendText(phone_number, message)
    # Sesscreator = Create(session=doctorName, catchQR= catchgenqr, logQR= True)
    # sess = Sesscreator.session
    # global client
    # try:
    #     sessStart = Sesscreator.start()
    #     if sessStart.waitForLogin():
    #         time.sleep(10)
    # except futures._base.TimeoutError():
    #     result = sessStart.sendText(phone_number, message)
    #     sessStart.close()
    # dumSess = sessStart.session
    result = openWhatsapp.client.sendText(phone_number, message)
    # time.sleep(5)
    
    # sessStart.close()
   
    
def whatsappApiEdit(patientName, doctorName, whatsappNumber, time_, date, clinicName):
    # reclient= openWhatsapp.client
    # from .views import catchgenqr
    phone_number = f"+91{whatsappNumber}" #phone_number = "+917904427507"  # or "+201016708170"
    message = f"Dear {patientName}, This is Dr.{doctorName}, from {clinicName}. Your Appointment has been changed to {time_} on {date}."
    # global creator
    # Sesscreator = Create(session=doctorName, catchQR= catchgenqr, logQR= True)
    # sess = Sesscreator.session
    # global client
    
    # sessStart = Sesscreator.start()
    # print("starting whatsapp session...")
    # if sessStart.waitForLogin():
    #     print("waiting for whatsapp session login...")
    #     time.sleep(10)
    #     print("browser must be open...")
    
    result = openWhatsapp.client.sendText(phone_number, message)
    # print("text message sent...")
    # time.sleep(5)
    
    # sessStart.close()
   
    
def whatsappMedia(whatsappNumber, pdfPathForWP, docName, patientName, prescDate):
    # from .views import catchgenqr
    phone_number = f"+91{whatsappNumber}"
    path = pdfPathForWP
    name = patientName
    caption = prescDate
    # global client
    # Sesscreator = Create(session=docName, catchQR= catchgenqr, logQR= True)
    # sess = Sesscreator.session
    # global client
    # try:
    #     sessStart = Sesscreator.start()
    #     if sessStart.waitForLogin():
    #         time.sleep(25)
    # except futures._base.TimeoutError():
    #     result = sessStart.sendFile(phone_number, path, name, caption )
    #     sessStart.close()    
    # dumSess = sessStart.session
    result = openWhatsapp.client.sendFile(phone_number, path, name, caption )
    # time.sleep(5)
  
    # sessStart.close()
 
    
    
    
    
    
    
    # message = openWhatsapp.client.sendMessageOptions()


    # # for pc in psutil.process_iter():
    # #     try:
    # #         print(pc.cmdline())
    # #     except psutil.AccessDenied:
    # #         continue
        
    # # start client with your session name
    # your_session_name = "test"
    # # check_open_directory = False
    # creator = Create(session=your_session_name, check_open_directory = False )
    # # client = creator.start()
    # client = creator.start()
    # # Now scan Whatsapp Qrcode in browser

    # # check state of login
    # if creator.state != 'CONNECTED':
    #     raise Exception(creator.state)

    # phone_number = whatsappNumber # or "+201016708170"
    # message = '''Hello From WPP WhatsApp Test Code !
    # A reminder from Dr Nandha kumar Dental clinic. Your Appointment has been fixed on 12 July 23 at 6pm and Don't forget your prescription!! '''

    # # Simple message
    # result = client.sendText(phone_number, message)
    # chrome_process = psutil.Process(1300)
    # info = chrome_process.info()
    # print(info)