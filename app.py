import time
import random
from pygame import mixer  # Load the popular external library
mixer.init()
mixer.music.load('notification.mp3')
words = ["Work", "Country", "Army", "Company", "Love", "Duty", "Girl", "Eat", "Decide", "Beat", "Fight", "Lie", "Give", "Enjoy", "Careful", "Success", "Trust", "Solve", "Story", "Break", "Fear", "Chair", "Defeat", "Enemy", "Garden", "Faith", "Help", "Cinema", "Money", "Peace", "Delay", "Character", "Travel", "Journey", "Ghost", "Respect", "Life", "Poor", "Use", "Climb", "Problem", "Attempt", "Moon", "Happy", "Books", "Rest", "Short", "Design", "Cooperate", "Descipline", "Plan", "Neglect", "Win", "Honesty", "Machine", "Afraid", "Load", "Think", "Hobby", "Obtain", "Idea", "Morality", "Innovation", "Strong", "Attack", "Continuous", "Punctuality", "Slip", "Drop", "Snake", "Award", "Achieve", "Assist", "Action", "Agree", "Avoid", "Alone", "Ambition", "Appeal", "Air", "Bed", "Blood", "Patient", "Beautiful", "Rose", "Weak", "Information", "Computer", "Green", "Horse", "Room", "Snake", "Wild", "Sex", "Window", "Graceful", "Women", "Hate", "Copy", "Home", "Able", "Excuse", "Luck", "War", "Home", "Playground", "Sports", "Sad", "Worry", "Army", "Music", "Health", "Custom", "Affection", "Fortune", "Fault", "Responsible", "Withdraw", "Tired", "Risk", "Boat", "Lead", "System", "Serious", "Save", "Jump", "Differ", "Warrior", "Hero", "Heroism", "Breakdown", "Lockdown", "Quarantine", "Corona", "Disaster", "Fake", "Pendamic", "Infection", "Instrument", "Gorgeous", "Marriage", "Divorce", "Wife", "Daughter", "Crowd", "Lonely", "Coward", "Example", "Smartphone", "Google", "Social Media", "Media", "Hilarious", "Prey", "Hunt", "Live", "Car", "Satellite", "Drunk", "Accident"]
random.shuffle(words)
for i in range(len(words)):    
    mixer.music.play()
    print(words[i])
    time.sleep(10)