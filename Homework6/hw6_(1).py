###########################################

#
# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively


#testing:
name = 'Ken'
symptoms = ['headache', 'toothache', 'fever', 'cough', 'anosmia']
pat1 = Patient(name, symptoms)

pat1.name        
pat1.symptoms


#
# 1.2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.
class Patient:
    def __init__(self, name: str, symptoms: list):
        self.name = name
        self.symptoms = symptoms
        
    def add_test(self, test_name: str, test_result: bool):
        self.test_name = test_name
        self.test_result = test_result


#testing:
pat1.add_test('covid', False)
print(pat1.test_name)
print(pat1.test_result)

#
# 1.3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and ncreases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']

class Patient:
    def __init__(self, name: str, symptoms: list):
        self.name = name
        self.symptoms = symptoms
        
    def add_test(self, test_name: str, test_result: bool):
        self.test_name = test_name
        self.test_result = test_result

    def has_covid(self):
        self._proba = 0.05
        try:
            if (self.test_name == 'Covid') & (self.test_result == True):
                self._proba = 0.99
                return self._proba
            elif (self.test_name == 'Covid') & (self.test_result == False):
                self._proba = 0.01
                return self._proba
        except AttributeError:
            if any(x in self.symptoms for x in ['fever', 'cough', 'anosmia']):
                self._proba += 0.1*len(self.symptoms)
                return self._proba
            else:
                return self._proba
                
# Testing
p1 = Patient("Andres", ["Fever"])
print(p1.name)
print(p1.symptoms)

print('')
p1.has_covid()
print(p1.has_covid())

print('')
p1.add_test('Covid', True)
print(p1.test_name)
print(p1.test_result)
print(p1.has_covid())

print('')
p1.add_test('Covid', False)
print(p1.has_covid())

######################

# 2. In this exercise you will make an English Deck class made of Card classes
# 
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.
class Card:
    def __init__(self, suit: str, value: float):
        self.suit = suit
        self.value = value
        
#test:
heart7 = Card('hearts', 9)
print(heart7.suit)
print(heart7.value)



# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit and value. When a card is drawn, the card should be removed from the deck.

import random 

class Deck: 
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        eng_deck = []
        
        for i in range(len(suits)):
            for j in range(len(values)):
                card = [suits[i], values[j]]
                card = tuple(card)
                eng_deck.append(card)
                
        self.current_deck = eng_deck
        
    def shuffle(self):
        random.shuffle(self.current_deck)
        return self.current_deck
    
    def draw(self):
        card_drawn = random.choice(self.current_deck)
        
        element_to_be_removed = [card_drawn]
        for element in element_to_be_removed:
            self.current_deck.remove(element)
        return card_drawn
        
        
#Testing
test = Deck() #<- Instantiates
test.current_deck #<- show full English deck
len(test.current_deck ) #<- 52

test.shuffle() #<- shuffles deck
test.draw() #<- draws random card and removes it from current deck
len(test.current_deck ) #<- 51


###################

# 3. In this exercise you will create an interface that will serve as template 
# for different figures to compute their perimeter and surface. 

from abc import ABC, abstractmethod
import math 

# 3.1 Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimiter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.
class PlaneFigure(ABC):
    @abstractmethod
    def compute_perimeter(self):
        pass
    
    @abstractmethod    
    def compute_surface(self):
        pass
    

# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and has as parameters in the constructor "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height). Implement the abstract methods with the formula of the triangle.
class Triangle(PlaneFigure):
    def __init__(self, base, c1, c2, h):
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.h = h
    
    def compute_perimeter(self):
        return self.base + self.c1 + self.c2
    
    def compute_surface(self):
        return 0.5*self.base*self.h


#testing:
test = Triangle(2, 1, 0.75, 0.2)
test.compute_perimeter()
test.compute_surface()



# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" and has as parameters in the constructor "a", "b" (sides of the rectangle). Implement the abstract methods with the formula of the rectangle.
class Rectangle(PlaneFigure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def compute_perimeter(self):
        return 2*self.a + 2*self.b
        
    def compute_surface(self):
        return self.a*self.b


#testing:
test = Rectangle(2,5)
test.compute_perimeter()
test.compute_surface()



# 3.4 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.
class Circle(PlaneFigure):
    def __init__(self, radius):
        self.radius = radius
    
    def compute_perimeter(self):
         return 2*math.pi*self.radius
        
    def compute_surface(self):
        return math.pi*self.radius**2
    
#testing:    
test = Circle(0.75)
test.compute_perimeter()
test.compute_surface()    
    

#checking:    
issubclass(Triangle, PlaneFigure)
issubclass(Rectangle, PlaneFigure)
issubclass(Circle, PlaneFigure)
issubclass(Deck, PlaneFigure)

