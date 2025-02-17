from django.shortcuts import render

# Create your views here.
def cv_view(request):
    context = {
        'name': 'Clely Voyena Fernandes',
        'email': 'cvf9554@nyu.edu',
        'phone': '347-567-4268',
        'education': [
            {'degree': 'B.Tech. Computer & Communication Engineering', 'institution': 'Manipal University Jaipur', 'year': '2020'},
            {'degree': 'M.S. Computer Science', 'institution': 'New York University', 'year': '2024'},
        ],
        # 'experience': [
        #     {'position': 'Software Developer', 'company': 'TechCorp', 'years': '2022-2024'},
        #     {'position': 'AI Researcher', 'company': 'AI Labs', 'years': '2024-Present'},
        # ],
        'skills': ['Python', 'Django', 'Machine Learning', 'Web Development']
    }
    return render(request, 'cvapp/cv.html', context)