from django.db import models
from Cryptodome.Hash import SHA256
from codecs import encode,decode
from django.utils import timezone


class Doctor(models.Model):
    name = models.CharField(unique = True, max_length = 30, blank = False, null = False)
    address = models.CharField(max_length = 2000)
    contactNumber = models.CharField(unique = True, max_length = 10, blank = False, null = False)
    email = models.EmailField(unique = True, max_length = 255)
    specialization = models.CharField(max_length = 100)
    passwordHash = models.CharField(max_length = 64)
    emailHash = models.CharField(max_length = 64)
    educationalQualification = models.CharField(max_length = 100)
    clinicName = models.CharField( max_length = 200)

    def __str__(self):
        return "Name : " + self.name + " Address : " + self.address + " Contact : " + self.contactNumber + " Email : " + self.email + " Specialization : " + self.specialization + "educationalQualification" + self.educationalQualification + "clinicName" + self.clinicName
    class Meta:
        db_table = 'healthcentre_doctor'

class doctorlogo(models.Model):
    doctorid = models.ForeignKey(Doctor, related_name = "docid", on_delete = models.CASCADE, db_column = 'doctorid')
    docname = models.CharField(max_length = 100)
    logo = models.ImageField(upload_to=r'static\HealthCentre\images', null=True, blank=True)
    # HealthCentre\static\HealthCentre\images
class Patient(models.Model):
    name = models.CharField(unique = True, max_length = 30)
    address = models.CharField(max_length = 2000)
    contactNumber = models.CharField(max_length = 10, db_column = 'contactnumber')
    email = models.EmailField(unique = True, max_length = 255, null= True, blank= True)
    rollNumber = models.CharField(max_length = 8, db_column = 'rollnumber') 
    passwordHash = models.CharField(max_length = 64, db_column = 'passwordhash')
    emailHash = models.CharField(max_length = 64, db_column = 'emailhash')  
    doctorid = models.ForeignKey(Doctor, related_name = "doctorid", on_delete = models.CASCADE, db_column = 'doctorid')
    doctorname = models.CharField(max_length = 100)


    def __str__(self):
        return "Name : " + self.name + " Address : " + self.address + " Contact : " + self.contactNumber + " Email : " + self.email + " doctorname : " + self.doctorname
    class Meta:
        db_table = 'healthcentre_patient'
        # db_column = 'contactnumber', 'rollnumber', 'passwordhash', 'emailhash'

class Medicine(models.Model):
    medicinename = models.CharField(max_length= 200)
    beforeafter = models.CharField(max_length= 200)
    morning = models.CharField(max_length= 200, blank= True)
    afternoon = models.CharField(max_length= 200, blank= True)
    night   = models.CharField(max_length= 200, blank= True)

    def __str__(self):
        return "\nmedicinemame :" + str(self.medicinename) + "\nbeforeafter :" + str(self.beforeafter) + "\nmorning :" + str(self.morning) + "\nafternoon :" + str(self.afternoon) + "\nnight :" + str(self.night) + "\n\n"
    class Meta:
        db_table = 'healthcentre_medicine'

class timeofday(models.Model):
    timeoftheday = models.CharField(max_length = 12)
    
    def __str__(self):
        return "\ntimeoftheday :" + str(self.timeoftheday) + '\n\n'
    class Meta:
        db_table = 'healthcenter_timeofday'
class Prescription(models.Model):
    prescriptionText = models.CharField(max_length = 2000, default = "", db_column = 'prescriptiontext')
    prescribingDoctor = models.CharField(max_length= 2000, default= "", db_column = 'prescribingdoctor')
    prescribingPatient = models.CharField(max_length= 2000, default= "", db_column = 'prescribingpatient')
    doctor = models.ForeignKey(Doctor, related_name = "doctorRecords", on_delete = models.CASCADE, db_column = 'doctor_id')
    patient = models.ForeignKey(Patient, related_name = "patientRecords", on_delete = models.CASCADE, db_column = 'patient_id')
    # beforeafter = models.CharField(max_length= 10)
    medicine    = models.ManyToManyField(to= Medicine)
    MornAftNight = models.ManyToManyField(to= timeofday)
    NoOfDays = models.CharField(max_length=10, db_column = 'noofdays')
    timestamp = models.DateTimeField(auto_now_add=True)
    isNew = models.BooleanField(default = True, db_column = 'isnew')
    isCompleted = models.BooleanField(default = False, db_column = 'iscompleted')
    symptoms = models.CharField(max_length = 2000)

    def __str__(self):
        return "\nDoctor :" + str(self.doctor) + "\n\nPatient :" + str(self.patient) + "\n\nPrescription : \n\n" + self.prescriptionText  + "\nNoOfDays :" + str(self.NoOfDays) + "\n\n" #+ "\nMedicine :" + str(self.medicine)
    class Meta:
        db_table = 'healthcentre_prescription'

class Appointment(models.Model):
    # id = models.AutoField(primary_key=True)
    time = models.TimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    subject = models.CharField(max_length=2000)
    notes = models.TextField()
    doctorPres = models.ForeignKey(Doctor, related_name = "doctorPrescRecords", on_delete = models.CASCADE, db_column= 'doctorpres')
    patientPres = models.ForeignKey(Patient, related_name = "patientPrescRecords", on_delete = models.CASCADE, db_column= 'patientpres')
    appointmentpatient = models.CharField(max_length=2000, default = "")
    appointmentdoctor  = models.CharField(max_length=2000, default= "")
    AppointmentTimeStamp = models.DateTimeField(default = timezone.now, db_column = 'appointmenttimestamp')#auto_now_add = True 
#auto_now_add = True, 
    def __str__(self):
        return "\nDoctorId :" + str(self.doctorPres) + "\nPatientId :" + str(self.patientPres) + "\nDoctor :" + str(self.appointmentdoctor) + "\n\nPatient" + str(self.appointmentpatient) +"\n\nDate :"+ str(self.date) + "\n\nTime :" + str(self.time) + "\n\nSubject :" + str(self.subject) + "\n\nnotes :" + str(self.notes) + "\n\n"
    class Meta:
        db_table = 'healthcentre_appointment'

def passwordHasher(userPassword):
    """Function to return the hash of the password using SHA-256. Input is the password of the user in string."""
    userPassword = userPassword
    SHA256Engine = SHA256.new()
    userPassword = userPassword.encode()
    SHA256Engine.update(userPassword)
    passwordHash = SHA256Engine.digest()
    passwordHash = encode(passwordHash, 'hex')
    passwordHash = decode(passwordHash, 'utf-8')
    return passwordHash


def emailHasher(userEmail):
    """Function to return the hash of the email using SHA-256. Input is the email of the user in string."""
    userEmail = userEmail
    SHA256Engine = SHA256.new()
    userEmail = userEmail.encode()
    SHA256Engine.update(userEmail)
    emailHash = SHA256Engine.digest()
    emailHash = encode(emailHash, 'hex')
    emailHash = decode(emailHash, 'utf-8')
    return emailHash
    
