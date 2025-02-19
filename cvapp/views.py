from django.shortcuts import render

def cv_view(request):
    context = {
        'name': 'Clely Voyena Fernandes',
        'email': 'cvf9554@nyu.edu',
        'phone': '+1 347 569 4268',
        'github': 'https://github.com/clely19',
        'linkedin': 'https://linkedin.com/in/clely-fernandes',
        
        'education': [
            {'degree': 'M.S. Computer Science', 'institution': 'New York University', 'year': 'Aug 2024 – May 2026'},
            {'degree': 'B.Tech. Computer Science', 'institution': 'Manipal University Jaipur', 'year': 'July 2020 – May 2024'},
        ],

        'skills': {
            'programming_languages': ['Java', 'Dart', 'C', 'Kotlin', 'Python', 'JavaScript', 'SQL'],
            'web_development': ['HTML5', 'CSS3', 'Bootstrap', 'React.js'],
            'mobile_dev': ['Flutter', 'Firebase Integration'],
            'tools_frameworks': ['Git', 'GitHub CLI', 'Node.js', 'Bokeh']
        },

        'projects': [
            {'name': 'Sentiment Analysis of New York Times Articles', 
             'duration': 'Sept 2024 - Dec 2024', 
             'description': 'Built an analysis tool for sentiment detection, contributing to data-driven decision-making.'},
            
            {'name': 'A Smart Agricultural App', 
             'duration': 'Dec 2023 - April 2024', 
             'description': 'Developed an IoT-based real-time sensor data monitoring system using Flutter and Firebase, improving data accuracy by 40%.'},
        ],

        'experience': [
            {'position': 'Freelance App Developer', 'company': 'Self-Employed (Rajasthan, India)', 'years': 'Oct 2022 – Jan 2023',
             'responsibilities': [
                 'Designed a fitness-oriented mobile app offering workout plans and sports-specific guidance, enhancing user adoption by 25%.',
                 'Collaborated with designers and developers, demonstrating strong multitasking and communication skills.'
             ]},
        ],

        'coursework': [
            {'name': 'Software Engineering', 'term': 'Jan 2025 – May 2025', 
             'description': 'Applied Agile methodologies in a collaborative team,using sprints to enhance customer onboarding.'},
             {'name': 'Design & Analysis of Algorithms', 'term': 'Jan 2025 – May 2025', 
             'description': 'Optimized application support using advanced problem-solving techniques.'},
             {'name': 'Application Security', 'term': 'Jan 2025 – May 2025', 
             'description': 'Automated and troubleshot security workflows using GitHubActions in a production support setting.'},
        ],

        'extracurricular': [
            {'role': 'Junior Board Member', 'organization': 'TechSHRM at NYU', 'years': 'Jan 2025 - Present',
             'responsibilities': ['Increased student engagement & outreach through event coordination.']}
        ]
    }

    return render(request, 'cvapp/cv.html', context)
