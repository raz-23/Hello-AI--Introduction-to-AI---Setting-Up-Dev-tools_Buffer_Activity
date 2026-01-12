import webbrowser

print("Hello! I am AI Bot.")

name = input("What's your name? : ").strip()
print(f"Nice to meet you, {name}!")

while True:
    mood = input("\nHow are you feeling? (happy/sad/ok): ").strip().lower()

    # Emotion-based response
    if mood == "happy":
        print("That's nice to hear 😊")
    elif mood == "sad":
        print("I hope you feel better soon 😔")
    else:
        print("Alright! Let's continue 🙂")

    site_name = input(
        "Which website do you want to open? (example: google, youtube): "
    ).strip().lower()

    url = f"https://www.{site_name}.com"
    print(f"Opening {url} now...")
    webbrowser.open(url)

    again = input("\nDo you want to continue? (yes/no): ").strip().lower()
    if again != "yes":
        print(f"It was nice chatting with you, {name}. Bye!")
        break
