from django.shortcuts import render, redirect
from django.contrib import messages
from Base.models import Contact


def home(request):
    return render(request, 'home.html')


def about(request):
    context = {
        "name": "Harsh Raj",
        "title": "Software Developer",
        "bio": "Passionate about DSA, Web Development, and Problem Solving.",

        "skills": ["C++", "Python", "Django", "React", "SQL"],

        # 🔥 UPDATED LeetCode DATA (matches UI)
        "leetcode": {
            "total": 503,
            "total_questions": 3893,
            "easy": "288 / 935",
            "medium": "186 / 2037",
            "hard": "29 / 921",
            "profile": "https://leetcode.com/u/HarshRaj142006/"
        },

        "gfg": {
            "total": 332,
            "total_questions": 3893,
            "basic": "26 / 500",
            "easy": "98 / 935",
            "medium": "190 / 2037",
            "hard": "18 / 921",
            "profile": "https://www.geeksforgeeks.org/profile/darkgod" 
            },

        "achievements": [
            "Solved 800+ DSA problems",
            "5⭐ in Problem Solving",
            "Built full-stack projects",
            "Participated in coding contests"
        ]
    }

    return render(request, "about.html", context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')

        # ✅ Name validation
        if not name or not (2 <= len(name) <= 30):
            messages.error(request, 'Name must be between 2 and 30 characters')
            return redirect('home')

        # ✅ Email validation
        if not email or "@" not in email or "." not in email:
            messages.error(request, 'Invalid email address')
            return redirect('home')

        # ✅ Phone validation
        if not number or not (10 <= len(number) <= 12 and number.isdigit()):
            messages.error(request, 'Invalid phone number')
            return redirect('home')

        # ✅ Save to DB
        Contact.objects.create(
            name=name,
            email=email,
            number=number,
            content=content
        )

        messages.success(request, 'Message sent successfully ✅')
        return redirect('home')

    return render(request, 'home.html')