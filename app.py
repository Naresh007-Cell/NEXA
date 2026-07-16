from brain.chat import ask_nexa
from memory.memory import remember, recall

print("=" * 50)
print("🤖 NEXA AI Assistant v2")
print("=" * 50)
print("Type 'exit' to quit.\n")

messages = []

name = recall("name")
if name:
    print(f"👋 Welcome back {name}!")

while True:

    user = input("You: ")

    # Exit
    if user.lower() in ["exit", "quit", "bye"]:
        print("\nNEXA: Goodbye 👋")
        break

    # Remember Name
    if user.lower().startswith("my name is "):
        name = user[11:].strip()
        remember("name", name)
        print(f"\nNEXA: Nice to meet you {name}. I will remember your name.\n")
        continue

    # Telugu Mode
    if any(ch in user for ch in "అఆఇఈఉఊఎఏఐఒఓఔకఖగఘచజటడతదపబమయరలవశసహళక్ష"):
        user = (
            "Reply only in Telugu. "
            "Do not use English words or English letters.\n\n"
            + user
        )

    # Tanglish Mode
    elif any(word in user.lower() for word in [
        "telugu",
        "telugu lo",
        "telugu matladu",
        "telugu matladu ra",
        "telugu cheppu"
    ]):
        user = (
            "Reply only in Telugu written using English letters "
            "(Tanglish). Example: 'Ela unnava?', 'Tinnava?', "
            "Never use Telugu script.\n\n"
            + user
        )

    messages.append(
        {
            "role": "user",
            "content": user
        }
    )

    reply = ask_nexa(messages)

    print("\nNEXA:", reply)
    print()

    messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )