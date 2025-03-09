from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from .models import Student_profile, AdmissionForm, Class, Subject,ExamMarks,Faculty
import json
from django.views.decorators.csrf import csrf_exempt


def index(request):
    if not request.user.is_authenticated:
        return redirect('/signin')

    # Count students by class
    bca_count = AdmissionForm.objects.filter(student_class='BCA').count()
    bba_count = AdmissionForm.objects.filter(student_class='BBA').count()
    bba_ism_count1 = AdmissionForm.objects.filter(student_class='BBA-ISM').count()
    bba_ism_count2 = AdmissionForm.objects.filter(student_class='BBA (ISM)').count()
    bba_ism_count3 = AdmissionForm.objects.filter(student_class='BBA ISM').count()
    bba_ism_count=bba_ism_count1+bba_ism_count2+bba_ism_count3
    # Total student count
    total_student_count = AdmissionForm.objects.count()

    # Pass the counts to the template
    return render(request, 'index.html', {
        'bca_count': bca_count,
        'bba_count': bba_count,
        'bba_ism_count': bba_ism_count,
        'total_student_count': total_student_count
    })

# SignIn view
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
       
    return render(request, 'signin.html')

# SignUp view
def signup_user(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        
        # Check if fields are empty
        if not username or not email or not password:
            return JsonResponse({"error": "All fields are required."}, status=400)

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists."}, status=400)

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already exists."}, status=400)

        # Create user and login
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('/')

    return render(request, 'signup.html')

# Logout view
def logout_user(request):
    logout(request)
    return redirect('/signin')

# Add Marks view
def add_marks_user(request):
    return render(request, 'marks_adding.html')

def save_marks(request):
    if request.method == 'POST':
        class_name = request.POST.get('class_name', 'BCA')  # Default to 'BCA' if not provided
        semester = request.POST.get('semester')
        subject_id = request.POST.get('subject')

        # Get the subject object
        try:
            subject = Subject.objects.get(id=subject_id)
        except Subject.DoesNotExist:
            # Handle the case if subject doesn't exist
            return render(request, 'teacher_add_marks.html', {'error': 'Subject not found'})

        # Loop through the students' marks and save them
        for key, value in request.POST.items():
            if key.startswith('marks_'):  # Look for marks fields
                enrollment_no = key.split('_')[1]  # Extract the enrollment number
                marks = value

                # Get all students with the same enrollment number
                students = Student_profile.objects.filter(enrollment_no=enrollment_no)

                # Check if students exist with the same enrollment number
                if students.exists():
                    for student in students:
                        # Check if the marks for this student, subject, and semester already exist
                        if not ExamMarks.objects.filter(
                            student=student,
                            subject=subject,
                            semester=semester,
                            class_name=class_name
                        ).exists():
                            # Save the marks to the ExamMarks model if it doesn't exist
                            ExamMarks.objects.create(
                                student=student,
                                subject=subject,
                                marks=marks,
                                semester=semester,
                                class_name=class_name
                            )
                else:
                    continue  # If no student found with the same enrollment number, skip

    return render(request, 'marks_adding.html')

def get_subjects(request):
    if request.method == "POST":
        data = json.loads(request.body)
        class_name = data.get('class_name')
        semester = data.get('semester')

        selected_class = Class.objects.filter(name=class_name, semester=semester).first()

        if selected_class:
            subjects = selected_class.subjects.all()
            subjects_data = [{'id': subject.id, 'name': subject.name} for subject in subjects]
            return JsonResponse({'subjects': subjects_data})
        
        return JsonResponse({'error': 'No subjects found for the selected class and semester.'}, status=404)

# Fetch students for a specific class and semester
def get_students(request):
    if request.method == "POST":
        data = json.loads(request.body)
        class_name = data.get('class_name')
        semester = data.get('semester')

        students = Student_profile.objects.filter(class_name=class_name, semester=semester)
        students_data = [{'name': student.name, 'enrollment_no': student.enrollment_no} for student in students]
        return JsonResponse({'students': students_data})



# Add Student view
def student_profile_user(request):
    if request.method == 'POST':
        full_name = request.POST.get('name')
        enrollment_no = request.POST.get('enrollment_no')
        class_name = request.POST.get('class_names')
        semester = request.POST.get('semester')
        blood_group = request.POST.get('blood_group')
        address = request.POST.get('address')
        contact_no = request.POST.get('contact_no')
        about_yourself = request.POST.get('about_yourself')

        student_profile = Student_profile.objects.create(
            name=full_name,
            enrollment_no=enrollment_no,
            class_name=class_name,
            semester=semester,
            blood_group=blood_group,
            address=address,
            contact_no=contact_no,
            about_yourself=about_yourself
        )
        return render(request, 'student_profile_Edit.html')
    return render(request, 'student_profile_Edit.html')

def profile(request):
    return render(request, 'profile.html')

def class_subject_add(request):
    return render(request, 'class_subject_add.html')

def reviwes_user(request):
    return render(request, 'reviwes.html')

def tables(request):
    return render(request, 'tables.html')

def analitycs_user(request):
    return render(request, 'analitics.html')

def edit_profile_user(request):
    return render(request, 'student_profile_Edit.html')

def spcam_admin(request):
    return render(request, 'spcam_admin.html')

def admission_form_view(request):
    if request.method == 'POST':
        form_no = request.POST.get('form_no')
        date = request.POST.get('date')
        student_class = request.POST.get('class')
        full_name = request.POST.get('full_name')
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation', '')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation', '')
        nationality = request.POST.get('nationality')
        state = request.POST.get('state', '')
        district = request.POST.get('district')
        city = request.POST.get('city')
        mobile = request.POST.get('mobile')
        parent_mobile = request.POST.get('parent_mobile')
        dob = request.POST.get('dob')
        blood_group = request.POST.get('blood_group')
        race_religion = request.POST.get('race_religion')
        aadhar = request.POST.get('aadhar')
        email = request.POST.get('email')
        caste = request.POST.get('caste')
        school_name = request.POST.get('school_name')
        school_district = request.POST.get('school_district')
        school_city = request.POST.get('school_city')
        board = request.POST.get('board')
        stream = request.POST.get('stream')
        total_marks = request.POST.get('total_marks')
        obtained_marks = request.POST.get('obtained_marks')
        percentage = request.POST.get('percentage')
        place = request.POST.get('place')
        form_date = request.POST.get('date')

        photograph = request.FILES.get('photograph')
        application_form = request.FILES.get('application_form')
        higher_secondary_certificate = request.FILES.get('higher_secondary_certificate')
        caste_certificate = request.FILES.get('caste_certificate')
        ssc_hsc_marksheets = request.FILES.get('ssc_hsc_marksheets')
        aadhar_card = request.FILES.get('aadhar_card')
        marriage_certificate = request.FILES.get('marriage_certificate')
        other_qualifications = request.FILES.get('other_qualifications')

        admissionform = AdmissionForm(
            form_no=form_no,
            date=date,
            student_class=student_class,
            full_name=full_name,
            father_name=father_name,
            father_occupation=father_occupation,
            mother_name=mother_name,
            mother_occupation=mother_occupation,
            nationality=nationality,
            state=state,
            district=district,
            city=city,
            mobile=mobile,
            parent_mobile=parent_mobile,
            dob=dob,
            blood_group=blood_group,
            race_religion=race_religion,
            aadhar=aadhar,
            email=email,
            caste=caste,
            school_name=school_name,
            school_district=school_district,
            school_city=school_city,
            board=board,
            stream=stream,
            total_marks=total_marks,
            obtained_marks=obtained_marks,
            percentage=percentage,
            place=place,
            form_date=form_date,
            photograph=photograph,
            application_form=application_form,
            higher_secondary_certificate=higher_secondary_certificate,
            caste_certificate=caste_certificate,
            ssc_hsc_marksheets=ssc_hsc_marksheets,
            aadhar_card=aadhar_card,
            marriage_certificate=marriage_certificate,
            other_qualifications=other_qualifications
        )
        admissionform.save()
        

    return render(request, 'spcam_admin.html')

def create_class_subjects(request):
    if request.method == 'POST':
        class_name = request.POST.get('class_name')
        semester = request.POST.get('semester')
        subjects = request.POST.get('subjects').split(',')

        # Create class
        class_obj = Class.objects.create(name=class_name, semester=semester)

        # Create subjects and associate them with the class
        for subject in subjects:
            cleaned_subject = subject.strip()
            if cleaned_subject:  # Avoid creating empty subjects
                Subject.objects.create(name=cleaned_subject, class_obj=class_obj)

    
    return render(request, 'class_subject_add.html')


def add_teacher(request):
    if request.method=='POST':
        photo = request.FILES.get('photo')
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        experience = request.POST.get('experience')
        education=request.POST.get('education')
        function=request.POST.get('function')
        hire_date=request.POST.get('hire_date')
        research=request.POST.get('research')
        publications_national = request.POST.get('publications_national')
        publications_international =request.POST.get('publications_international')
        seminars_national = request.POST.get('seminars_national')
        seminars_international = request.POST.get('seminars_international')
        outreach = request.POST.get('outreach')

        #create a new teacher record
        teacher=Faculty(
            photo=photo,
            full_name=full_name,
            email=email,
            subject=subject,
            experience=experience,
            education=education,
            function=function,
            hire_date=hire_date,
            research=research,
            publications_national=publications_national,
            publications_international=publications_international,
            seminars_national=seminars_national,
            seminars_international=seminars_international,
            outreach=outreach
        )
        teacher.save()
        
        # return redirect('tables.html') # Redirect to a teacher list page (replace with your URL)

    # return render(request, 'tables.html')
        

    # Fetch all faculty details to display
    teachers = Faculty.objects.all()
    return render(request, 'tables.html', {'teachers': teachers})


# def faculty_details(request):
#     # Fetching all faculty details from the Faculty model
#     faculties = Faculty.objects.all()
#     return render(request, 'tables.html', {'faculties': faculties})
# def faculty_details(request):
#     teachers = Faculty.objects.all()  # Database se sabhi records fetch karte hain
#     print(teachers)  # Console pe check karne ke liye
#     return render(request, 'tables.html', {'teachers': teachers})  # teachers naam ka context pass kar rahe hain
def view_student_profile(request):
    student = None
    error_message = None
    marks = None  # Initialize marks variable

    if request.method == 'POST':
        enrollment_number = request.POST.get('enrollment_number')
        semester = request.POST.get('semester')

        # Print the values to debug
        print(f"Received Enrollment Number: {enrollment_number}")
        print(f"Received Semester: {semester}")

        # Fetch student details based on enrollment number
        try:
            student = Student_profile.objects.get(enrollment_no=enrollment_number)
        except Student_profile.DoesNotExist:
            error_message = "Student not found"
            print("Student not found in database.")

        # Fetch marks if student exists and semester is provided
        if student and semester:
            try:
                # Ensure the semester is treated as an integer if required by your model
                semester = int(semester)
                marks = ExamMarks.objects.filter(student=student, semester=semester)
                
                # Debug the fetched marks count
                print(f"Found {marks.count()} marks for Semester {semester}.")
            except Exception as e:
                print(f"Error while fetching marks: {e}")

    # Render the page with student info and marks
    return render(request, 'student_profile.html', {
        'student': student,
        'error_message': error_message,
        'marks': marks  # Pass marks to the template
    })
