from django.shortcuts import render, redirect
from .models import JobRole, Resume
from .utils import extract_text_from_pdf, extract_text_from_docx, extract_skills
from django.contrib.auth.decorators import login_required
import random

# Resource Mapping for skills
SKILL_RESOURCES = {
    "Python": [
        "https://www.python.org/doc/",
        "https://www.youtube.com/watch?v=_uQrJ0TkZlc", 
        "https://www.freecodecamp.org/learn/scientific-computing-with-python/"
    ],
    "Django": [
        "https://docs.djangoproject.com/en/stable/",
        "https://www.youtube.com/watch?v=F5mRW0jo-U4",
        "https://tutorial.djangogirls.org/en/"
    ],
    "HTML": [
        "https://developer.mozilla.org/en-US/docs/Web/HTML",
        "https://www.w3schools.com/html/",
        "https://www.freecodecamp.org/learn/2022/responsive-web-design/"
    ],
    "CSS": [
        "https://developer.mozilla.org/en-US/docs/Web/CSS",
        "https://css-tricks.com/",
        "https://www.freecodecamp.org/learn/2022/responsive-web-design/"
    ],
    "JavaScript": [
        "https://javascript.info/",
        "https://developer.mozilla.org/en-US/docs/Web/JavaScript", 
        "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/"
    ],
    "React": [
        "https://react.dev/learn",
        "https://www.youtube.com/watch?v=bMknfKXIFA8",
        "https://scrimba.com/learn/learnreact"
    ],
    "SQL": [
        "https://www.w3schools.com/sql/",
        "https://mode.com/sql-tutorial/",
        "https://www.khanacademy.org/computing/computer-programming/sql"
    ],
    "Git": [
        "https://git-scm.com/doc",
        "https://www.atlassian.com/git/tutorials",
        "https://learngitbranching.js.org/"
    ],
    "Java": [
        "https://docs.oracle.com/en/java/",
        "https://www.baeldung.com/java-tutorial",
        "https://www.codecademy.com/learn/learn-java"
    ],
    "Spring Boot": [
        "https://spring.io/guides/gs/spring-boot/",
        "https://www.baeldung.com/spring-boot",
        "https://www.youtube.com/watch?v=9SGDpanrc8U"
    ],
    "TensorFlow": [
        "https://www.tensorflow.org/learn",
        "https://www.coursera.org/specializations/tensorflow-in-practice",
        "https://www.youtube.com/watch?v=tPYj3fFJGjk"
    ],
    "Selenium": [
        "https://www.selenium.dev/documentation/",
        "https://www.guru99.com/selenium-tutorial.html",
        "https://testautomationuniversity.applitools.com/"
    ]
}

def upload_resume(request):
    # Optional: require login to save data permanently, but let's allow guest for now or redirect
    # if not request.user.is_authenticated: return redirect('login') 
    
    if request.method == 'POST':
        file = request.FILES.get('resume')
        role_id = request.POST.get('role')
        
        if file and role_id:
            job_role = JobRole.objects.get(id=role_id)
            
            # Create resume object
            resume = Resume.objects.create(file=file, job_role=job_role)
            
            # If user is logged in, associate it
            if request.user.is_authenticated:
                resume.user = request.user
                resume.save()
            
            # Parsing
            file_path = resume.file.path
            text = ""
            try:
                if file.name.endswith('.pdf'):
                    text = extract_text_from_pdf(file_path)
                elif file.name.endswith('.docx'):
                    text = extract_text_from_docx(file_path)
            except Exception as e:
                print(f"Error parsing: {e}")
                
            resume.parsed_content = text
            
            # Skills
            found, missing = extract_skills(text, job_role.required_skills)
            resume.extracted_skills = found
            resume.missing_skills = missing
            
            # Score
            total_skills = len(job_role.required_skills)
            if total_skills > 0:
                score = (len(found) / total_skills) * 100
                resume.match_score = int(score)
            
            resume.save()
            return redirect('take_test', resume_id=resume.id)
            
    roles = JobRole.objects.all()
    return render(request, 'upload.html', {'roles': roles})

def results(request, resume_id, test_score):
    resume = Resume.objects.get(id=resume_id)
    
    recommendations = []
    if resume.missing_skills:
        for skill in resume.missing_skills:
            # Get specific links if we have them, else generic search
            links = SKILL_RESOURCES.get(skill, [
                f"https://www.google.com/search?q=free+{skill}+course",
                f"https://www.youtube.com/results?search_query=learn+{skill}",
                f"https://www.udemy.com/courses/search/?q={skill}&price=price-free-courses"
            ])
            
            recommendations.append({
                'skill': skill,
                'links': links # passing list of 3 links
            })
            
    context = {
        'resume': resume,
        'test_score': test_score,
        'recommendations': recommendations
    }
    return render(request, 'results.html', context)
