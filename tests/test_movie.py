import pytest
from viewing_party.person import Person
# class Person:
#     def __init__(self, name, watched, friends, subscriptions):
#         self.name = name
#         self.watched = watched
#         self.friends = friends
#         self.subscriptions = subscriptions

#     def add_watched(self,movie):
#         self.watched.append(movie)
#         return self.watched
    
#     def get_num_watched(self):
#         return len(self.watched)
def test_1_valid_input():
    person1 = Person("Cheetah","Titanic","Lion","Hulu")
    # Arrange
    assert person1.name == "Cheetah"
    assert person1.watched == "Titanic"
    # Act

    # Assert
