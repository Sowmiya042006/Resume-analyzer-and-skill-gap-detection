from django.shortcuts import render, redirect
from .models import Question, TestSession
from analyzer.models import Resume

def take_test(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    questions = Question.objects.filter(job_role=resume.job_role)
    
    if request.method == 'POST':
        score = 0
        total = questions.count()
        
        for q in questions:
            selected_option = request.POST.get(f'question_{q.id}')
            if selected_option == q.correct_answer:
                score += 1
                
        # Create Session
        TestSession.objects.create(
            resume=resume,
            score=score,
            total_questions=total
        )
        
        # Calculate percentage for display
        final_score_percent = int((score / total) * 100) if total > 0 else 0
        
        return redirect('results', resume_id=resume.id, test_score=final_score_percent)

    return render(request, 'test.html', {'resume': resume, 'questions': questions})
