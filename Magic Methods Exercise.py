import csv
import random

class Astronaut:
    """Astronaut class"""

    def __init__(self, name, flight_hr, status, year = None, group = None, birthdate = None, birthplace = None, 
                gender = None, almamater = None, undergraduate = None, graduate = None, military_rank = None,
                military_branch = None, space_flight = None, space_walk = None, space_walk_hr = None, 
                missions = None, death_date = None, death_mission = None):
        self.__name = name
        self.__flight_hr = flight_hr
        self.__status = status
        self.__year = year
        self.__group = group
        self.__birthdate = birthdate
        self.__birthplace = birthplace
        self.__gender = gender
        self.__almamater = almamater
        self.__undergraduate = undergraduate
        self.__graduate = graduate
        self.__military_rank = military_rank
        self.__military_branch = military_branch
        self.__space_flight = space_flight
        self.__space_walk = space_walk
        self.__space_walk_hr = space_walk_hr
        self.__missions = missions
        self.__death_date = death_date
        self.__death_mission = death_mission

    @property
    def name(self):
        return self.__name

    @property
    def flight_hr(self):
        return self.__flight_hr

    @property
    def status(self):
        return self.__status

    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @flight_hr.setter
    def flight_hr(self, new_flight_hr):
        self.__flight_hr = new_flight_hr

    @status.setter
    def status(self, new_status):
        self.__status = new_status

    def __eq__(self,other):
        if (self.__flight_hr == other.__flight_hr):
            return self.__flight_hr == other.__flight_hr
        else:
            return False

    def __gt__(self,other):
        if (self.__flight_hr > other.__flight_hr):
            return self.__flight_hr > other.__flight_hr
        else:
            return False
    
    def __ge__(self,other):
        if (self.__flight_hr >= other.__flight_hr):
            return self.__flight_hr >= other.__flight_hr
        else:
            return False
    
    def __str__(self):
        return (self.__name + "," + self.__status)

   
data = list()
with open("astronauts.csv") as csvfile:
    for line in csv.DictReader(csvfile):
        astronaut = Astronaut(line['Name'], line['Space Flight (hr)'], line['Status'])
        data.append(astronaut)

print(vars(data[0]))
print(random.choice(data) == random.choice(data))
print(random.choice(data) > random.choice(data))
print(random.choice(data) >= random.choice(data))

for astronaut in data:
    print(astronaut)