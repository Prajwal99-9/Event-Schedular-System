# test_events.py

from events import Event
import datetime

def test_create_event():
    title = "Test Event"
    description = "This is a test event"
    start_time = datetime.datetime(2023, 1, 1, 10, 0)
    end_time = datetime.datetime(2023, 1, 1, 12, 0)
    
    event = Event(title, description, start_time, end_time)
    
    assert event.title == title
    assert event.description == description
    assert event.start_time == start_time
    assert event.end_time == end_time
    
def test_event_ordering():
    # Create some sample events
    event1 = Event("A", "", datetime.datetime(2023, 1, 1, 10, 0), datetime.datetime(2023, 1, 1, 12, 0))
    event2 = Event("B", "", datetime.datetime(2023, 1, 2, 10, 0), datetime.datetime(2023, 1, 2, 12, 0))
    event3 = Event("C", "", datetime.datetime(2023, 1, 3, 10, 0), datetime.datetime(2023, 1, 3, 12, 0))
    
    events = [event2, event3, event1]
    
    events.sort(key=lambda x: x.start_time)
    
    assert events == [event1, event2, event3]