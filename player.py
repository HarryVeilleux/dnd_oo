"""Example Player class to demonstrate object-oriented D&D character generation"""
import random


class Player:
    """Basic things to know about classes:
    
    All functions defined in this class are called "methods". They always take a 
    special argument called "self" as their first argument, which lets Python
    access all of the variables you've set on the instance so far (one of the
    most important benefits of object-oriented structures). Methods are called by 
    creating an instance of the class, then using dot notation.

    Attributes are also set and retrieved using dot notation (e.g. if p is an instance
    of the Player class, p.abilities['charisma'] will retrieve the character's Charisma
    score).
    
    Methods that start and end with double underscores are special built-in methods
    (often affectionately called "dunders"). Defining a dunder typically tells 
    Python something special about the class (details below each).
    """
    def __init__(self):
        """This dunder is called whenever you create an instance of the class.

        Use it to define code you want to run every time you create a new Player,
        like setting default attribute values.
        """
        self.abilities = {
            "charisma": 0,
            "constitution": 0,
            "dexterity": 0,
            "intelligence": 0,
            "strength": 0,
            "wisdom": 0
        }
        self.height = 0
        self.weight = 0
        self.class_ = []  
        # note I named this attribute "class_" instead of "class", because "class" is 
        # a built-in keyword in Python
        self.languages = []
        self.race = None

    def set_abilities(self, randomize: bool = True):
        """Generate six random ability score values and assign them.

        If randomize is True (default), scores are assigned randomly. Otherwise, the 
        user is prompted to set them.
        """
        def generate_score():
            """I would typically define this helper function elsewhere (like how you
            defined d6 at the top of your scripts then called later), but I'm putting 
            it here to make it easier to see.
            """
            rolls = [random.randint(1, 6) for _ in range(4)]
            for i, v in enumerate(rolls):
                if v == 1:  # reroll once
                    rolls[i] = random.randint(1, 6)
            return sum(sorted(rolls)[1:])
        
        scores = [generate_score() for _ in range(6)]
        if randomize:  # randomly assign
            random.shuffle(scores)  # shuffle randomly orders a list in place
            for ability, score in zip(self.abilities, scores):
                self.abilities[ability] = score
        else:  # prompt user to choose
            for ability in self.abilities:
                while not self.abilities[ability]:  # keep prompting until we've set a value
                    print(f"Scores to choose from: {scores}")
                    score = int(input(f"What should should we assign to {ability}? "))
                    if score in scores:
                        self.abilities[ability] = score
                        scores.remove(score)
                    else:
                        print("Invalid choice!")

    def set_race(self, randomize: bool = True):
        """Set race from list of valid races."""
        races = ["High Elf", "Human"]  # just doing a couple to start
        if randomize:
            self.race = random.choice(races)
        else:
            while not self.race:  # keep prompting until we've set a race
                print(f"Races to choose from: {races}")
                race = input("What race should we set? ")
                if race in races:
                    self.race = race
                else:
                    print("Invalid choice!")

    def set_racial_traits(self):
        """Apply racial traits (e.g. ability bonuses) based on race.
        
        This assumes that race and ability scores are already set, and does nothing except 
        notify the user if either/both are not set.

        I'm defining this as a separate method to show how a method can use values
        set in other methods without having to pass those values to the method.
        """
        if any(not v for v in self.abilities.values()):
            print("Abilities are not set! Call set_abilities method first.")
        elif not self.race:
            print("Race is not set! Call set_race method first.")
        else:
            if self.race == "High Elf":
                self.abilities["charisma"] += 1
                self.abilities["dexterity"] += 2


def setup_player(randomize: bool = True):
    """Instantiate and return an instance of the Player class."""
    p = Player()
    if randomize:
        p.set_abilities()
        p.set_race()
        p.set_racial_traits()
    else:
        p.set_abilities(False)
        p.set_race(False)
        p.set_racial_traits()
    return p
