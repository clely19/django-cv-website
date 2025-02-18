from django.shortcuts import render

def cv_view(request):
    context = {
        'name': 'Clely Voyena Fernandes',
        'email': 'clelyfernandes@outlook.com',
        'phone': '+1 347 569 4268',
        'github': 'https://github.com/clely19',
        'linkedin': 'https://linkedin.com/in/clely-fernandes',
        
        'education': [
            {'degree': 'M.S. Computer Science', 'institution': 'New York University', 'year': 'Aug 2024 – May 2026'},
            {'degree': 'B.Tech. Computer Science', 'institution': 'Manipal University Jaipur', 'year': 'July 2020 – May 2024'},
        ],

        'skills': [
            'Java', 'Dart', 'C', 'Kotlin', 'Python', 'JavaScript', 'SQL',
            'HTML5', 'CSS3', 'Bootstrap', 'React.js',
            'Flutter', 'Firebase Integration',
            'Git', 'GitHub CLI', 'Node.js', 'Bokeh'
        ],

        'projects': [
            {'name': 'Sentiment Analysis of New York Times Articles', 
             'duration': 'Sept 2024 - Dec 2024', 
             'description': 'Built an analysis tool for sentiment detection, contributing to data-driven decision-making.'},
            
            {'name': 'A Smart Agricultural App', 
             'duration': 'Dec 2023 - April 2024', 
             'description': 'Developed an IoT-based real-time sensor data monitoring system using Flutter and Firebase, improving data accuracy by 40%.'},
            
            {'name': 'Fitness App', 
             'duration': 'May 2023 - July 2023', 
             'description': 'Designed and deployed a cross-platform fitness app with real-time user support, leading to a 30% increase in customer engagement.'},
        ],

        'experience': [
            {'position': 'Freelance App Developer', 'company': 'Self-Employed (Rajasthan, India)', 'years': 'Oct 2022 – Jan 2023',
             'responsibilities': [
                 'Designed a fitness-oriented mobile app offering workout plans and sports-specific guidance, enhancing user adoption by 25%.',
                 'Collaborated with designers and developers, demonstrating strong multitasking and communication skills.',
                 'Provided application support by diagnosing and resolving technical issues.'
             ]},
        ],

        'coursework': [
            {'name': 'Design & Analysis of Algorithms', 'term': 'Jan 2025 – May 2025', 
             'description': 'Optimized application support using advanced problem-solving techniques. Enhanced process optimization by analyzing real-world algorithmic efficiencies in software development.'},
            
            {'name': 'Application Security', 'term': 'Jan 2025 – May 2025', 
             'description': 'Automated and troubleshot security workflows using GitHub Actions in a production support setting. Identified and resolved security vulnerabilities pre-deployment.'},
            
            {'name': 'Software Engineering', 'term': 'Jan 2025 – May 2025', 
             'description': 'Applied Agile methodologies in a collaborative team, using sprints to enhance customer onboarding. Executed product updates and feature rollouts, improving end-user satisfaction through feedback-driven enhancements.'},
        ],

        'extracurricular': 'Junior Board - TechSHRM at New York University (Jan 2025 - Present). Playing an instrumental role in the Communications & Event Coordinating Team by increasing student engagement & outreach.',
    }

    return render(request, 'cvapp/cv.html', context)
