person=None
people=[]

while person!='':
    person=input("Enter invitee's name (or just enter to finish): ")
    if person!='':
        people.append(person)

for each in people:
    print(each+ ", please attend our party this Saturday!")

