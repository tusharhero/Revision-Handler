from datetime import datetime
from json import load, dump


JSON_PATH = "example.json"

# Print Current Date
current_time = datetime.now()
print(current_time.strftime("%m/%d/%Y, %H:%M"))

short_data_view = {}

def get_short_view():
    for subject in data.copy():
        for i, chapter in enumerate(data[subject]):
            short_data_view[f"{subject[:2]}{i+1}"] = data[subject][chapter]  

def detailed_view():
    for subject in data.copy():
        print(subject.upper())
        for i, chapter in enumerate(data[subject]):
            print(f" - {chapter.capitalize()}")
            for subtopic in data[subject][chapter]:
                print(f"\t - {subtopic}  ({data[subject][chapter][subtopic]})")
        print()


with open(JSON_PATH) as f:
    data = load(f)


get_short_view()
running = True
while running:
    cmd = input(": ").lower()

    if cmd in ["exit", "quit", "q", "close"]:
        running = False

    elif cmd in ["detailed view", "dv"]:
        detailed_view()

    elif cmd in short_data_view.keys():
        for subtopic in short_data_view[cmd]:
            print(f" - {subtopic} ({short_data_view[cmd][subtopic]})")

    elif cmd in ["subject", "subjects", "s"]:
        for subject in data:
            print(subject.upper())

print(data)