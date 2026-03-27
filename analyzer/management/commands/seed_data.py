from django.core.management.base import BaseCommand
from analyzer.models import JobRole
from assessment.models import Question

class Command(BaseCommand):
    help = 'Seeds database with expanded Job Roles and Questions'

    def handle(self, *args, **kwargs):
        # Define Roles and 10 Questions each
        data = {
            "Web Developer": {
                "skills": ["HTML", "CSS", "JavaScript", "React", "Django", "Python", "SQL", "Git"],
                "questions": [
                    ("What does CSS stand for?", ["Cascading Style Sheets", "Computer Style Systems", "Creative Style Sheets", "Colorful Style Sheets"], "Cascading Style Sheets"),
                    ("Which HTML tag is used to define an internal style sheet?", ["<css>", "<script>", "<style>", "<link>"], "<style>"),
                    ("Which Django file is used to configure database settings?", ["views.py", "models.py", "urls.py", "settings.py"], "settings.py"),
                    ("In JavaScript, which symbol is used for comments?", ["//", "#", "<!--", "**"], "//"),
                    ("What is the correct syntax for a React component?", ["function MyComponent() {}", "class MyComponent", "Both A and B", "None"], "Both A and B"),
                    ("Which HTTP method is used to retrieve data?", ["GET", "POST", "PUT", "DELETE"], "GET"),
                    ("What does DOM stand for?", ["Document Object Model", "Data Object Mode", "Digital Ordinance Model", "None"], "Document Object Model"),
                    ("Which command creates a new Django app?", ["startapp", "startproject", "newapp", "createapp"], "startapp"),
                    ("What is the purpose of 'git status'?", ["Shows changes", "Commits changes", "Pushes code", "Deletes branch"], "Shows changes"),
                    ("What is JSON?", ["JavaScript Object Notation", "Java Sorting Object", "JavaScript Options Naming", "None"], "JavaScript Object Notation"),
                ]
            },
            "Data Analyst": {
                "skills": ["Python", "SQL", "Pandas", "NumPy", "Matplotlib", "Excel", "Tableau", "PowerBI"],
                "questions": [
                    ("Which library is primarily used for data manipulation in Python?", ["NumPy", "Pandas", "Matplotlib", "Seaborn"], "Pandas"),
                    ("What does SQL stand for?", ["Structured Query Language", "Strong Question Language", "Structured Question List", "Simple Query Language"], "Structured Query Language"),
                    ("Which command allows you to view the first 5 rows of a DataFrame?", ["head()", "tail()", "top()", "first()"], "head()"),
                    ("What is a primary key?", ["Unique identifier", "Duplicate value", "Foreign key", "None"], "Unique identifier"),
                    ("Which chart is best for showing trends over time?", ["Line Chart", "Pie Chart", "Bar Chart", "Scatter Plot"], "Line Chart"),
                    ("In Excel, which function sums a range?", ["SUM", "ADD", "TOTAL", "COUNT"], "SUM"),
                    ("Which Python library is for numerical computing?", ["NumPy", "Pandas", "Requests", "Flask"], "NumPy"),
                    ("What is 'Data Cleaning'?", ["Fixing errors/missing data", "Deleting all data", "Backup data", "None"], "Fixing errors/missing data"),
                    ("Which SQL keyword sorts the result?", ["ORDER BY", "SORT BY", "GROUP BY", "ALIGN"], "ORDER BY"),
                    ("What is a CSV file?", ["Comma Separated Values", "Common Systematic Values", "Computer Saved Videos", "None"], "Comma Separated Values"),
                ]
            },
            "Frontend Developer": {
                "skills": ["HTML", "CSS", "JavaScript", "React", "Vue", "Tailwind", "Git", "Redux"],
                "questions": [
                    ("What property changes text color in CSS?", ["color", "font-color", "text-color", "fg-color"], "color"),
                    ("Which HTML5 tag is used for the main content?", ["<main>", "<content>", "<section>", "<body>"], "<main>"),
                    ("What is React's virtual DOM?", ["A lightweight copy of DOM", "A heavy database", "A server engine", "None"], "A lightweight copy of DOM"),
                    ("How do you center a div using Flexbox?", ["justify-content: center; align-items: center;", "text-align: center;", "margin: auto;", "float: center;"], "justify-content: center; align-items: center;"),
                    ("What is the purpose of Redux?", ["State Management", "Routing", "Styling", "Testing"], "State Management"),
                    ("Which directive is used for loops in Vue.js?", ["v-for", "ng-repeat", "*ngFor", "loop"], "v-for"),
                    ("What is the CSS Box Model?", ["Margin, Border, Padding, Content", "Header, Footer, Main", "Flex, Grid, Block", "None"], "Margin, Border, Padding, Content"),
                    ("Which unit is relative to the font-size of the root element?", ["rem", "em", "px", "%"], "rem"),
                    ("How do you comments in CSS?", ["/* comment */", "// comment", "<!-- comment -->", "# comment"], "/* comment */"),
                    ("What event fires when an input loses focus?", ["blur", "focus", "change", "click"], "blur"),
                ]
            },
            "Python Developer": {
                "skills": ["Python", "Django", "Flask", "FastAPI", "SQL", "Git", "Docker", "REST API"],
                "questions": [
                    ("How do you define a function in Python?", ["def my_func():", "function my_func():", "func my_func():", "define my_func():"], "def my_func():"),
                    ("What data type is immutable?", ["Tuple", "List", "Dictionary", "Set"], "Tuple"),
                    ("How do you install a package using pip?", ["pip install name", "python install name", "npm install name", "pip get name"], "pip install name"),
                    ("What is a decorator?", ["A function that modifies another function", "A tool for styling", "A class attribute", "None"], "A function that modifies another function"),
                    ("Which framework is known for being micro?", ["Flask", "Django", "Pyramid", "Tornado"], "Flask"),
                    ("What dunder method is used for string representation?", ["__str__", "__init__", "__len__", "__repr__"], "__str__"),
                    ("What keyword is used for error handling?", ["try...except", "do...catch", "try...catch", "errors...handle"], "try...except"),
                    ("What is PEP 8?", ["Python Style Guide", "Python Compiler", "Python Database", "None"], "Python Style Guide"),
                    ("How do you check current directory in OS module?", ["os.getcwd()", "os.pwd()", "os.dir()", "os.path()"], "os.getcwd()"),
                    ("What is a generator?", ["Function yielding values", "Function returning list", "A loop", "None"], "Function yielding values"),
                ]
            },
            "Java Developer": {
                "skills": ["Java", "Spring Boot", "Hibernate", "SQL", "Maven", "Git", "Microservices"],
                "questions": [
                    ("Which keyword is used to inherit a class?", ["extends", "implements", "inherits", "super"], "extends"),
                    ("What is the size of int in Java?", ["4 bytes", "2 bytes", "8 bytes", "1 byte"], "4 bytes"),
                    ("Which collection does not allow duplicates?", ["Set", "List", "Queue", "ArrayList"], "Set"),
                    ("What acts as an entry point for a Java application?", ["main method", "start method", "init method", "run method"], "main method"),
                    ("What is JVM?", ["Java Virtual Machine", "Java Verification Mode", "Java Visual Model", "None"], "Java Virtual Machine"),
                    ("Which annotation marks a Spring Boot application?", ["@SpringBootApplication", "@SpringApp", "@BootApp", "@Application"], "@SpringBootApplication"),
                    ("What is the default value of a boolean?", ["false", "true", "null", "0"], "false"),
                    ("Which concept is NOT part of OOP?", ["Compilation", "Inheritance", "Polymorphism", "Encapsulation"], "Compilation"),
                    ("How do you handle exceptions?", ["try-catch", "do-while", "if-else", "for-loop"], "try-catch"),
                    ("What is 'final' keyword used for?", ["To make constant", "To make variable", "To make public", "None"], "To make constant"),
                ]
            },
            "AI/ML Engineer": {
                "skills": ["Python", "TensorFlow", "PyTorch", "Keras", "Scikit-Learn", "Pandas", "Mathematics"],
                "questions": [
                    ("Which algorithm is used for classification?", ["Logistic Regression", "Linear Regression", "K-Means", "PCA"], "Logistic Regression"),
                    ("What is Overfitting?", ["Model performs well on training data but bad on new data", "Model performs bad on everything", "Model is too simple", "None"], "Model performs well on training data but bad on new data"),
                    ("Which library is widely used for Deep Learning?", ["TensorFlow", "Pandas", "NumPy", "Matplotlib"], "TensorFlow"),
                    ("What does NLP stand for?", ["Natural Language Processing", "Neural Learning Paths", "New Linear Processing", "None"], "Natural Language Processing"),
                    ("What is a Neuron?", ["Basic unit of Neural Network", "A python function", "A database key", "None"], "Basic unit of Neural Network"),
                    ("Supervised learning requires...?", ["Labeled data", "Unlabeled data", "No data", "Reinforcement"], "Labeled data"),
                    ("What is ‘k’ in K-Means clustering?", ["Number of clusters", "Number of steps", "Kernel size", "None"], "Number of clusters"),
                    ("Which metric works best for imbalanced data?", ["F1-Score", "Accuracy", "MSE", "MAE"], "F1-Score"),
                    ("What is a Tensor?", ["Multi-dimensional array", "A type of graph", "A database", "A server"], "Multi-dimensional array"),
                    ("Which activation function is used for binary classification?", ["Sigmoid", "ReLU", "Softmax", "Tanh"], "Sigmoid"),
                ]
            },
            "Quality Assurance (Tester)": {
                "skills": ["Selenium", "Java", "Python", "JIRA", "TestNG", "Manual Testing", "SQL"],
                "questions": [
                    ("What is a bug?", ["Error/Flaw in software", "A viral feature", "Correct code", "None"], "Error/Flaw in software"),
                    ("What does SDLC stand for?", ["Software Development Life Cycle", "System Design Life Code", "Software Design Logic Control", "None"], "Software Development Life Cycle"),
                    ("Which testing is done without checking code?", ["Black Box Testing", "White Box Testing", "Unit Testing", "Integration Testing"], "Black Box Testing"),
                    ("Selenium is used for...?", ["Web Automation", "Mobile App Testing", "Desktop App Testing", "API Testing"], "Web Automation"),
                    ("What is Regression Testing?", ["Testing after code changes", "Testing new features only", "Testing design", "None"], "Testing after code changes"),
                    ("What is a Test Case?", ["Set of conditions to verify a feature", "A bug report", "A project plan", "None"], "Set of conditions to verify a feature"),
                    ("Which tool is common for bug tracking?", ["JIRA", "Excel", "Notepad", "Paint"], "JIRA"),
                    ("What is UAT?", ["User Acceptance Testing", "Unit Analysis Testing", "User Access Tool", "None"], "User Acceptance Testing"),
                    ("What is Positive Testing?", ["Testing with valid data", "Testing with invalid data", "Testing blindly", "None"], "Testing with valid data"),
                    ("STLC stands for?", ["Software Testing Life Cycle", "System Testing Logic Code", "Simple Test Cycle", "None"], "Software Testing Life Cycle"),
                ]
            }
        }

        for role_name, info in data.items():
            role, created = JobRole.objects.get_or_create(
                title=role_name,
                defaults={'required_skills': info['skills']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created role: {role_name}"))
            else:
                 # Update skills if exists
                 role.required_skills = info['skills']
                 role.save()

            # Add Questions
            for q_text, options, ans in info['questions']:
                # Avoid duplicates
                if not Question.objects.filter(job_role=role, text=q_text).exists():
                    Question.objects.create(
                        job_role=role,
                        text=q_text,
                        options=options,
                        correct_answer=ans
                    )
                    
        self.stdout.write(self.style.SUCCESS('Successfully seeded extended database.'))
