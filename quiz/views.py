import random
from django.shortcuts import render
from django.http import JsonResponse
from .models import Question

def quiz(request):
    if request.method == 'POST':
        questions = Question.objects.filter(id__in=request.session['quiz_ids'])
        correct = 0
        answer_map = request.session.get('answer_map', {})
        for i, q in enumerate(questions):
            user_answer = int(request.POST.get(f'q{i}', 0))
            correct_option = answer_map.get(str(q.id))
            if user_answer == correct_option:
                correct += 1
        return render(request, 'quiz/result.html', {'score': correct, 'total': len(questions)})

    all_ids = list(Question.objects.values_list('id', flat=True))
    quiz_ids = random.sample(all_ids, 50) if len(all_ids) >= 50 else all_ids
    questions = list(Question.objects.filter(id__in=quiz_ids))
    random.shuffle(questions)
    
    randomized_questions = []
    answer_map = {}
    
    for q in questions:
        # Variantlarni asl tartibida saqlash
        options = [q.option1, q.option2, q.option3, q.option4]
        answer_map[str(q.id)] = q.correct  # To'g'ri javobni asl indeksi bilan saqlash
        
        randomized_questions.append({
            'id': q.id,
            'text': q.text,
            'options': options
        })
    
    request.session['quiz_ids'] = quiz_ids
    request.session['answer_map'] = answer_map
    return render(request, 'quiz/quiz.html', {'questions': randomized_questions})

def check_answer(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
    question_index = int(request.POST.get('question_index', -1))
    user_answer = int(request.POST.get('answer', 0))
    
    if question_index < 0 or user_answer < 1 or user_answer > 4:
        return JsonResponse({'error': 'Invalid input'}, status=400)
    
    questions = Question.objects.filter(id__in=request.session['quiz_ids'])
    question = list(questions)[question_index]
    answer_map = request.session.get('answer_map', {})
    correct_option = answer_map.get(str(question.id))
    
    # Get the correct answer text from the original options
    options = [question.option1, question.option2, question.option3, question.option4]
    correct_answer_text = options[question.correct - 1]
    
    return JsonResponse({
        'correct': user_answer == correct_option,
        'correct_answer': correct_answer_text
    })
