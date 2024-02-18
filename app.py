import datetime
import json

events = []

class Event:

    def __init__(self, title, description, start_time, end_time):
        self.title = title
        self.description = description 
        self.start_time = start_time
        self.end_time = end_time

def add_event():
    title = input("Enter event title: ")
    description = input("Enter event description: ")
    start_time = input("Enter event start time (YYYY-MM-DD HH:MM): ")
    start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M")
    end_time = input("Enter event end time (YYYY-MM-DD HH:MM): ") 
    end_time = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M")

    event = Event(title, description, start_time, end_time)
    events.append(event)

    print("Event added successfully!")
    print(event.__dict__)

    save_events()

def view_events():
    print("Here are all scheduled events:")
    for i, event in enumerate(events):
        print(f"{i+1}. {event.title} - {event.description}")
        print(f"From: {event.start_time} To: {event.end_time}")
        print()
    save_events()

def update_event():
   # Code to update event
   pass 

def delete_event():
   # Code to delete event
   pass
   
def save_events():
    with open('events.json', 'w') as f:
        json.dump([{**e.__dict__, 
                    'start_time': e.start_time.isoformat(),
                    'end_time': e.end_time.isoformat()} 
                   for e in events], f)

def load_events():
    try:
        with open('events.json', 'r') as f:
            events_data = json.load(f)
            for e in events_data:
                event = Event(e['title'], e['description'], 
                              datetime.datetime.fromisoformat(e['start_time']),
                              datetime.datetime.fromisoformat(e['end_time']))
                events.append(event)
    except:
        print("No events file found")
        pass
        
if __name__ == '__main__':

    load_events()
    
    while True:
        print("1. Add Event")
        print("2. View Events")
        print("3. Update Event")
        print("4. Delete Event")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_event()
        elif choice == '2':
            view_events()
        elif choice == '3':
            update_event()
        elif choice == '4':
            delete_event()
        elif choice == '5': 
            break
        else:
            print("Invalid choice!")