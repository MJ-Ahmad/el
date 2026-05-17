import os

# Base directory
base_dir = "el/docs/beginner"
os.makedirs(base_dir, exist_ok=True)

# Class content dictionary
classes = {
    "class1_greetings.md": """# Class 1: Greetings & Politeness

## New Words
- Hello
- Thank you
- Sorry
- Yes
- No

## Sentences
- Hello, how are you?
- Thank you very much.
- I am sorry.
- Yes, I understand.
- No, I don’t know.

## Practice
- Greet 5 people with "Hello".
- Say "Thank you" when someone helps you.
""",

    "class2_daily_needs.md": """# Class 2: Daily Needs & Small Conversations

## New Words
- Morning
- Night
- School
- Work
- Family

## Sentences
- Good morning, how are you?
- Good night, see you tomorrow.
- I go to school.
- I go to work.
- I love my family.

## Practice
- Use "Good morning" and "Good night" daily.
- Talk about your school or work in English.
""",

    "class3_time_place_feelings.md": """# Class 3: Time, Place & Feelings

## New Words
- Time
- Place
- Happy
- Sad
- Learn

## Sentences
- What time is it?
- This is my place.
- I am happy today.
- I am sad.
- I want to learn English.

## Practice
- Ask the time in English.
- Express your feelings (happy/sad).
- Say "I want to learn English" daily.
""",

    "class4_teacher_student.md": """# Class 4: Teacher–Student & Practice

## New Words
- Teacher
- Student
- Question
- Answer
- Practice

## Sentences
- I am a student.
- You are my teacher.
- Ask me a question.
- I will answer.
- I practice every day.

## Practice
- Roleplay: Teacher asks, student answers.
- Say "I practice every day" to build confidence.
""",

    "class5_storytelling.md": """# Class 5: Storytelling & Presentation

## New Words
- Story
- Talk
- Present
- Idea
- Confidence

## Sentences
- I will tell you a story.
- I want to talk in English.
- I will present my idea.
- This is a good idea.
- I speak with confidence.

## Practice
- Tell a 3–4 line story in English.
- Present your idea in 5 lines.
- Say "I speak with confidence" aloud.
"""
}

# Write files
for filename, content in classes.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# Create summary file
summary_content = """# Beginner Summary

In Classes 1–5, you learned:
- Basic greetings and politeness
- Daily needs and small conversations
- Time, place, and feelings
- Teacher–student roleplay
- Storytelling and presentation

👉 Outcome: You can now speak short sentences and basic conversations with confidence.
"""
with open(os.path.join(base_dir, "summary.md"), "w", encoding="utf-8") as f:
    f.write(summary_content)

print("✅ Class 1–5 content created successfully in docs/beginner/")
