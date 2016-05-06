import random as rand
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = location
        
    def get_number_of_species(self, animal):
        if animal not in self.species_types:
            return 0.0
        else:
            return self.species_types[animal]
         
    def get_location(self):
        return float(self.location[0]), float(self.location[1])
         
    def get_species_count(self):
        copy = {}
        for i in self.species_types:
            if self.species_types[i] != 0:
                copy[i] = self.species_types[i]
        return copy
        
    def get_name(self):
        return self.name
         
    def adopt_pet(self, species):
        self.species_types[species] -= 1


class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
         
    def get_name(self):
        return self.name
        
    def get_desired_species(self):
        return self.desired_species
        
    def get_score(self, adoption_center):
        return float(adoption_center.get_number_of_species(self.desired_species))


class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species
    
    def get_score(self, adoption_center):
        considered_total = 0
        for i in range(len(self.considered_species)):
            considered_total += adoption_center.get_number_of_species(self.considered_species[i])
        return adoption_center.get_number_of_species(self.desired_species) + 0.3*considered_total


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species
    
    def get_score(self, adoption_center):
        if adoption_center.get_number_of_species(self.desired_species) < 0.3*adoption_center.get_number_of_species(self.feared_species):
            return 0.0
        else:
            return adoption_center.get_number_of_species(self.desired_species) -0.3*adoption_center.get_number_of_species(self.feared_species)


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species
    
    def get_score(self, adoption_center):
        for i in self.allergic_species:
            if i in adoption_center.get_species_count():
                return 0.0
        return Adopter.get_score(self, adoption_center)


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness
    
    def get_score(self, adoption_center):
        allergic_rate = 1.0
        for i in self.medicine_effectiveness:
            if i in adoption_center.get_species_count():
                if self.medicine_effectiveness[i] < allergic_rate:
                    allergic_rate = self.medicine_effectiveness[i]
        return allergic_rate*Adopter.get_score(self, adoption_center)


class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location
    
    def get_linear_distance(self, to_location):
        import math
        x1 = self.location[0]
        y1 = self.location[1]
        x2 = to_location[0]
        y2 = to_location[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

    def get_score(self, adoption_center):
        import random
        distance = self.get_linear_distance(adoption_center.get_location())
        if distance < 1:
            return Adopter.get_score(self, adoption_center)
        elif distance >= 1 and distance < 3:
            return random.uniform(0.7, 0.9)*Adopter.get_score(self, adoption_center)
        elif distance >= 3 and distance < 5:
            return random.uniform(0.5, 0.7)*Adopter.get_score(self, adoption_center)
        elif distance >= 5:
            return random.uniform(0.1, 0.5)*Adopter.get_score(self, adoption_center)

    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    from operator import itemgetter
    my_list = []
    sorted_list =[]
    for i in list_of_adoption_centers:
        my_list.append([adopter.get_score(i), i.get_name(), i])
    b = sorted(my_list, key=itemgetter(1))
    c = sorted(b, key=itemgetter(0), reverse=True)
    for j in c:
        sorted_list.append(j[2])
    return sorted_list

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    from operator import itemgetter
    my_list = []
    sorted_list =[]
    for i in list_of_adopters:
        my_list.append([i.get_score(adoption_center), i.get_name(), i])
    b = sorted(my_list, key=itemgetter(1))
    c = sorted(b, key=itemgetter(0), reverse=True)
    for j in c:
        sorted_list.append(j[2])
    return sorted_list


adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat")

ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2,10))
ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8,-2))
ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))

# how to test get_ordered_adoption_center_list
get_ordered_adoption_center_list(adopter4, [ac,ac2,ac3,ac4,ac5,ac6])
# you can print the name and score of each item in the list returned

