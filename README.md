# Event-Schedular-System
An event scheduler system is a sophisticated software tool designed to streamline and organize the planning and execution of events. This comprehensive system efficiently manages various aspects of event management, from initial planning stages to post-event evaluations. 

Event Scheduler
This is a simple event scheduler application that allows users to add, view, update and delete events.

Features
Add events with title, description, start time and end time
View all scheduled events
Update existing events
Delete existing events
Persist events data in a JSON file
Usage
Run python app.py to start the application.

You will see a menu with options to:

Add event
View events
Update event
Delete event
Exit
Follow the prompts to create, view, update or delete events.

The events are saved to a events.json file. When the app starts, existing events are loaded from this file.

Event class
The Event class represents an event with the following properties:

title - Title of the event
description - Description text
start_time - Start datetime
end_time - End datetime
Functions
add_event() - Prompts user for event details and creates an Event object
view_events() - Prints details of all scheduled events
update_event() - Allows updating an existing event (not implemented yet)
delete_event() - Allows deleting an event (not implemented yet)
save_events() - Saves events to JSON file
load_events() - Loads events from JSON file
TODO
Implement update_event()
Implement delete_event()
