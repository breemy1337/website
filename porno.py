class Bird:
    def __init__(self, species, color, age):
        self.species = species
        self.color = color
        self.age = age    


class Parrot(Bird):
    def __init__(self, species, color, age, vocabulary_size):
        super().__init__(species, color, age)
        self.vocabulary_size = vocabulary_size
