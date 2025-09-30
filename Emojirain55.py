import random
import time
import os

emojis = ["😀", "😂", "😎", "😍", "🤩", "🤖", "🐍", "🔥", "⚡", "🌟"]

try:
    while True:
        # Clear screen (Windows = cls, Linux/Mac = clear)
        os.system("cls" if os.name == "nt" else "clear")
        
        # Print random emojis in a line
        line = "".join(random.choice(emojis) for _ in range(30))
        print(line)
        
        time.sleep(0.2)
except KeyboardInterrupt:
    print("\nStopped Emoji Rain ☔")
