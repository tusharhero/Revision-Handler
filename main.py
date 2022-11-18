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
    sub_i = 0
    for subject in data.copy():
        print(f"{sub_i} {subject.upper()}")
        sub_i += 1
        chapter_i = 0
        for i, chapter in enumerate(data[subject]):
            total_topics = 0
            topics_revised = 0
            subtopic_data = ""
            topic_i = 0

            # Gets topics revised in last week and prepare topics to print
            for subtopic in data[subject][chapter]:
                revised_date = data[subject][chapter][subtopic]
                total_topics += 1
                days_past = (
                    current_time - datetime.strptime(revised_date, "%m/%d/%Y")
                ).days

                if days_past <= 7:
                    topics_revised += 1
                subtopic_data += f"\t {str(topic_i)} - {subtopic}  ({revised_date})\n"
                topic_i += 1

            # Prints all info about chapter
            chapter_progress = int(topics_revised / total_topics * 100)
            print(f" - {chapter_i} : {chapter.capitalize()} ({chapter_progress}%)\n" + subtopic_data)
            chapter_i += 1
        print()

def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")

def start_editing():
    # print(f"    Select subject:")
    # for subject in data:
    #     print(f"    {subject.upper()}")

    # print()
    # # subject = input("   :").lower()
    # if subject not in data.keys():
    #     return

    # chapters = data[subject]
    # print(f"    Select chapter:")
    # for chapter in chapters:
    #     print(f"    {chapter.lower()}")
    # print()

    # chapter = input("   :").lower()
    # if chapter not in chapters.keys():
    #     return

    # subtopics = chapters[chapter]
    # print(f"")
    # for subtopic in subtopics:
    #     print(f"    {subtopic}")
    detailed_view()
    print("Enter the entry you want to edit in the format")
    print("K:S:C:T")
    print("Here K ==> Action ==> Add chaptername :AC, Edit chaptername: EC , Add subtopic: AT , Edit subtopicdate: EDT , Edit subtopic: ET")
    print("S ==> Subject index")
    print("C ==> Chapter index")
    print("T ==> subtopic index")
    command = input(" : ")
    args = command.split(":")
    K = str(args[0])
    S = int(args[1])
    C = int(args[2])
    T = int(args[3])
    print(K,S,C,T)

    if K == "EDT":
        
        subject = get_nth_key(data,S)
        chapter = get_nth_key(data[subject],C)
        subtopic = get_nth_key(data[subject][chapter],T)
        print(f"you are going to edit the date of subtopic '{subtopic}' in chapter '{chapter}' of '{subject}'")

        new_date = input("  date: ")

        if new_date.lower() == "today":
            new_date = current_time.strftime("%m/%d/%Y")

        data[subject][chapter][subtopic] = new_date
    
    if K == "ET":
        subject = get_nth_key(data,S)
        chapter = get_nth_key(data[subject],C)
        subtopic = get_nth_key(data[subject][chapter],T)
        print(f"you are going to edit the subtopic '{subtopic}' in chapter '{chapter}' of '{subject}'")

        subtopicname = input("  subtopic: ")
        data[subject][chapter][subtopicname]= data[subject][chapter].pop(subtopic)
    if K == "EC":
        subject = get_nth_key(data,S)
        chapter = get_nth_key(data[subject],C)
        print(f"you are going to edit the chapter name'{chapter}' of '{subject}'")

        chaptername = input("  subtopic: ")
        data[subject][chaptername] = data[subject].pop(chapter)
    
    if K == "AT":
        subject = get_nth_key(data,S)
        chapter = get_nth_key(data[subject],C)

        print(f"you are going to add a subtopic into chapter '{chapter}' of '{subject}'")
        newsubtopic = input("Enter the subtopic name: ")
        new_date = current_time.strftime("%m/%d/%Y")

        data[subject][chapter][newsubtopic] = new_date
    if K == "AC":
        subject = get_nth_key(data,S)

        print(f"you are going to add a chapter in '{subject}'")
        newchapter = input("Enter the chapter name: ")

        new_date = current_time.strftime("%m/%d/%Y")
        data[subject][newchapter] = {"Enter the topics here": new_date}





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
    elif cmd in ["edit", "e", "change"]:
        start_editing()
    elif cmd in ["h", "help"]:
        print(
            """
        [exit, quit, q, close] - close the program
        [detailed view, dv] - gets detailed view of every subject and chapters
        [subject, subjects, s] - displays all subject
        [editing, e, chage] - edit a date in subject
        [h, help] - displays this message
        """
        )

print(data)

with open(JSON_PATH, "w") as f:
    dump(data, f)
