import time
import random

sentences = [
    "Python is an amazing programming language.",
    "Artificial intelligence is shaping the future.",
    "Hard work beats talent when talent doesn’t work hard.",
    "Coding every day improves your logic and focus.",
    "Practice makes a programmer perfect."
]

def typing_test():
    sentence = random.choice(sentences)
    print("\n💬 Type this sentence exactly as shown below:\n")
    print(f"👉 {sentence}\n")
    input("Press Enter when you're ready... ")
    
    start_time = time.time()
    typed = input("\nStart typing here:\n")
    end_time = time.time()

    time_taken = end_time - start_time
    words = len(sentence.split())
    wpm = (words / time_taken) * 60

    print("\n⏱️ Time taken: {:.2f} seconds".format(time_taken))
    print("💨 Your typing speed: {:.2f} words per minute".format(wpm))

    # Accuracy check
    correct_chars = sum(1 for i, j in zip(sentence, typed) if i == j)
    accuracy = (correct_chars / len(sentence)) * 100
    print("🎯 Accuracy: {:.2f}%".format(accuracy))

typing_test()
