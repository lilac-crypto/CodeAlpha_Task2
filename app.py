from flask import Flask, render_template, request
from random import sample

app = Flask(__name__)

# Quiz bank with 30 questions, options and answers (answer is the correct option text)
quiz_bank = [
    {"question": "What is phishing?", "options": ["A sport", "A cyber attack", "A recipe", "A backup method"], "answer": "A cyber attack"},
    {"question": "Which is a common sign of a phishing email?", "options": ["Spelling mistakes", "Professional language", "Official domain", "Secure attachment"], "answer": "Spelling mistakes"},
    {"question": "What should you check in a suspicious email?", "options": ["Sender address", "Email color", "Attachment name", "Font size"], "answer": "Sender address"},
    {"question": "What does HTTPS indicate?", "options": ["Hacked website", "No encryption", "Encrypted connection", "Unsafe site"], "answer": "Encrypted connection"},
    {"question": "What is social engineering?", "options": ["Using new software", "Tricking people", "Designing apps", "Cloud storage"], "answer": "Tricking people"},
    {"question": "Which is a safe password?", "options": ["123456", "password", "MyName123", "Xy!8@kL#2"], "answer": "Xy!8@kL#2"},
    {"question": "What is a phishing website?", "options": ["Search engine", "Fake site mimicking real one", "Bank portal", "News site"], "answer": "Fake site mimicking real one"},
    {"question": "How to verify email authenticity?", "options": ["Click link", "Check domain", "Ignore it", "Forward to all"], "answer": "Check domain"},
    {"question": "Which of the following is NOT a phishing attempt?", "options": ["Fake login page", "Malware link", "Security training email", "Urgent bank alert"], "answer": "Security training email"},
    {"question": "What is spear phishing?", "options": ["Mass email", "Spam", "Targeted scam", "Clickbait"], "answer": "Targeted scam"},
    {"question": "What does a padlock symbol in browser mean?", "options": ["Dangerous site", "Encrypted connection", "Pop-up blocked", "No password"], "answer": "Encrypted connection"},
    {"question": "When should you report an email?", "options": ["Always", "When it’s suspicious", "After replying", "If no reply"], "answer": "When it’s suspicious"},
    {"question": "What’s the best reaction to phishing email?", "options": ["Reply politely", "Click all links", "Ignore and delete", "Mark as favorite"], "answer": "Ignore and delete"},
    {"question": "Why is public Wi-Fi risky?", "options": ["It's fast", "No password", "May allow data interception", "Too crowded"], "answer": "May allow data interception"},
    {"question": "Phishing tries to steal your?", "options": ["Food", "Login info", "TV", "Books"], "answer": "Login info"},
    {"question": "How can companies reduce phishing?", "options": ["Using firewalls", "User awareness training", "New laptops", "Larger inboxes"], "answer": "User awareness training"},
    {"question": "Why are phishing attacks dangerous?", "options": ["Time consuming", "Annoying", "Steal sensitive data", "Increase calls"], "answer": "Steal sensitive data"},
    {"question": "A typical phishing email might say?", "options": ["Hello friend", "Your account is compromised", "Happy birthday", "Watch this cat video"], "answer": "Your account is compromised"},
    {"question": "Is it safe to enter passwords on any site?", "options": ["Yes", "Only if asked", "Only on secure sites", "Always"], "answer": "Only on secure sites"},
    {"question": "What's a red flag in email?", "options": ["Greeting", "Formal language", "Urgency with link", "Grammatical correctness"], "answer": "Urgency with link"},
    {"question": "Which email is suspicious?", "options": ["newsletter@trusted.com", "security@amaz0n.com", "support@bank.com", "hello@college.edu"], "answer": "security@amaz0n.com"},
    {"question": "When in doubt about a link?", "options": ["Click it fast", "Verify it first", "Ignore forever", "Save it"], "answer": "Verify it first"},
    {"question": "Phishing attacks may use?", "options": ["Phone calls", "Emails", "Texts", "All of the above"], "answer": "All of the above"},
    {"question": "Why do hackers use fake websites?", "options": ["Fun", "For SEO", "To steal data", "To help you"], "answer": "To steal data"},
    {"question": "Which is safest action?", "options": ["Share passwords", "Use same password", "Use password manager", "Write on paper"], "answer": "Use password manager"},
    {"question": "Common phishing tactic is?", "options": ["Requesting urgent action", "Sending greetings", "Following up", "Ignoring emails"], "answer": "Requesting urgent action"},
    {"question": "How often should you change your passwords?", "options": ["Never", "Monthly", "When needed", "Every login"], "answer": "When needed"},
    {"question": "What’s a clone phishing?", "options": ["Duplicate app", "Copied email content", "Cloning hardware", "Fake ID"], "answer": "Copied email content"},
    {"question": "Which is safe practice?", "options": ["Click unknown links", "Disable antivirus", "Report phishing", "Use same password"], "answer": "Report phishing"},
    {"question": "What's a phishing lure?", "options": ["Bait used in scam", "Fish catching tool", "Real login page", "USB"], "answer": "Bait used in scam"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Get the submitted answers from the form
        submitted_answers = {}
        for i in range(1, 6):
            submitted_answers[f'q{i}'] = request.form.get(f'q{i}')
        
        # Check answers against the questions stored in the session or hidden field (better with session)
        # For simplicity, we will send questions as hidden inputs or use flask session (recommended)
        # Here, we just check answers against current quiz questions for demo
        # So we pass the questions as well in POST or save in session (here we'll just do a simple match)
        
        # We can store the 5 questions in session for production. Here assume we get them again (not recommended)
        # Instead, to keep consistent, store the questions in hidden inputs or session (I can add session code if needed)
        
        # For demo, calculate score assuming correct answers are passed in form as hidden fields named 'a1'..'a5'
        score = 0
        for i in range(1, 6):
            correct_answer = request.form.get(f'a{i}')
            user_answer = request.form.get(f'q{i}')
            if user_answer == correct_answer:
                score += 1
        
        return render_template('result.html', score=score)

    else:
        # On GET, show 5 random questions
        questions = sample(quiz_bank, 5)
        return render_template('quiz.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
