import pytest

from viewing_party.movie import Movie

def test_updated_rating():
    #Arrange
    movie1 = Movie("Everything","Sci Fi",10,["Netlfix"])
    #(self,title,genre,rating,host):
    #Act
    movie1.update_rating(100)

    #Assert
    assert movie1.rating == 100
