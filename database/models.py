from django.db import models

class Signup_user(models.Model):
    username = models.CharField(max_length=122)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

class Student_profile(models.Model):
    name = models.CharField(max_length=100)
    enrollment_no = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    semester = models.IntegerField()
    blood_group = models.CharField(max_length=3)
    address = models.TextField()
    contact_no = models.CharField(max_length=15)
    about_yourself = models.TextField()

    def __str__(self):
        return f"{self.name}"
    


class AdmissionForm(models.Model):
    form_no = models.CharField(max_length=20)
    date = models.DateField()
    student_class = models.CharField(max_length=20)
    full_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    father_occupation = models.CharField(max_length=255, blank=True, null=True)
    mother_name = models.CharField(max_length=255)
    mother_occupation = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=50)
    state = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    parent_mobile = models.CharField(max_length=15)
    dob = models.DateField()
    blood_group = models.CharField(max_length=10)
    race_religion = models.CharField(max_length=50)
    aadhar = models.CharField(max_length=20)
    email = models.EmailField()
    caste = models.CharField(max_length=50)
    school_name = models.CharField(max_length=255)
    school_district = models.CharField(max_length=100)
    school_city = models.CharField(max_length=100)
    board = models.CharField(max_length=50)
    stream = models.CharField(max_length=50)
    total_marks = models.IntegerField()
    obtained_marks = models.IntegerField()
    percentage = models.FloatField()
    place = models.CharField(max_length=100)
    form_date = models.DateField()

    photograph = models.FileField(upload_to='uploads/photograph/', blank=True, null=True)
    application_form = models.FileField(upload_to='uploads/application_form/', blank=True, null=True)
    higher_secondary_certificate = models.FileField(upload_to='uploads/higher_secondary_certificate/', blank=True, null=True)
    caste_certificate = models.FileField(upload_to='uploads/caste_certificate/', blank=True, null=True)
    ssc_hsc_marksheets = models.FileField(upload_to='uploads/ssc_hsc_marksheets/', blank=True, null=True)
    aadhar_card = models.FileField(upload_to='uploads/aadhar_card', blank=True, null=True)
    marriage_certificate = models.FileField(upload_to='uploads/marriage_certificate', blank=True, null=True)
    other_qualifications = models.FileField(upload_to='uploads/other_qualifications', blank=True, null=True)

    def __str__(self):
        return self.full_name

class Class(models.Model):
    name = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - Sem {self.semester}"


# Subject model to store subjects related to a specific class
class Subject(models.Model):
    name = models.CharField(max_length=100)
    class_obj = models.ForeignKey(Class, related_name='subjects', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ExamMarks(models.Model):
    student = models.ForeignKey(Student_profile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    semester = models.IntegerField(default=1)  # Provide a default value (e.g., 1)
    class_name = models.CharField(max_length=10, default="BCA") 
    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.marks}"
    

class Faculty(models.Model):
    photo = models.ImageField(upload_to='faculty/photos/', blank=True, null=True)  # Changed to ImageField if only images
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(default=0)  # Changed to PositiveIntegerField for non-negative values
    education = models.CharField(max_length=255)
    function = models.CharField(max_length=100)
    hire_date = models.DateField()
    research = models.TextField()
    publications_national = models.PositiveIntegerField(default=0)  # Used PositiveIntegerField
    publications_international = models.PositiveIntegerField(default=0)
    seminars_national = models.PositiveIntegerField(default=0)
    seminars_international = models.PositiveIntegerField(default=0)
    outreach = models.TextField()

    def __str__(self):
        return self.full_name
