class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def add_participant():
        new_ppl = input("Enter the full name of new participant: ")
        return str(event1) + str(new_ppl)
        #print(str(event1) + str(new_ppl))
        

    def get_participant_count():
        global count
        count += 1
        getting_count = int(event1 + count)
        print(getting_count)

event1 = Event('Alice Doe', '01/01/24')
count = 0


action = input("What would you like to do? (add/get count/exit): ")
if action == "add":
    Event.add_participant()
elif action == "get count":
    Event.get_participant_count()
elif action == "exit":
    print("Exiting system")