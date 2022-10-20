from datetime import datetime
from json import load, dump


JSON_PATH = "example.json"

# Print Current Date
current_time = datetime.now()
print(f"Time - {current_time.strftime('%m/%d/%Y, %H:%M')}")

short_data_view = {}


def get_short_view():
    for subject in data.copy():
        for i, chapter in enumerate(data[subject]):
            short_data_view[f"{subject[:2]}{i+1}"] = data[subject][chapter]


def detailed_view():
    for subject in data.copy():
        print(subject.upper())
        for i, chapter in enumerate(data[subject]):
            total_topics = 0
            topics_revised = 0
            subtopic_data = ""

            # Gets topics revised in last week and prepare topics to print
            for subtopic in data[subject][chapter]:
                revised_date = data[subject][chapter][subtopic]
                total_topics += 1
                days_past = (
                    current_time - datetime.strptime(revised_date, "%m/%d/%Y")
                ).days

                if days_past <= 7:
                    topics_revised += 1
                subtopic_data += f"\t - {subtopic}  ({revised_date})\n"

            # Prints all info about chapter
            chapter_progress = int(topics_revised / total_topics * 100)
            print(f" - {chapter.capitalize()} ({chapter_progress}%)\n" + subtopic_data)
        print()


with open(JSON_PATH) as f:
    data = load(f)

detailed_view()
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
