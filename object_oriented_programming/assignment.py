"""
OOP - Actors and Plays
Practice with classes, getters/setters with validation, composition, and __str__.
See ASSIGNMENT.md for the original prompt.
"""


# ------------------------------------------------------------
# PART 1 - Actor Class
# ------------------------------------------------------------

class Actor:
    """Represents a single actor with a name, age, and height."""

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    # --- Getters ---

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_height(self):
        return self.height

    # --- Setters (with validation) ---

    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        if new_age >= 0:
            self.age = new_age
        else:
            print("Age cannot be less than 0")

    def set_height(self, new_height):
        if new_height > 0:
            self.height = new_height
        else:
            print("Height must be greater than 0")

    def __str__(self):
        return f"Actor: {self.name} | Age: {self.age} | Height: {self.height} in"


# ------------------------------------------------------------
# PART 2 - Play Class
# ------------------------------------------------------------

class Play:
    """A play with a title, lead actor, runtime in minutes, and premiere year."""

    def __init__(self, title, lead_actor, length_min, year):
        self.title = title
        self.lead_actor = lead_actor
        self.length_min = length_min
        self.year = year

    # --- Getters ---

    def get_title(self):
        return self.title

    def get_lead_actor(self):
        return self.lead_actor

    def get_length_min(self):
        return self.length_min

    def get_year(self):
        return self.year

    # --- Setters (with validation) ---

    def set_title(self, new_title):
        self.title = new_title

    def set_lead_actor(self, new_actor):
        self.lead_actor = new_actor

    def set_length_min(self, new_length):
        if new_length <= 0:
            print("Length must be greater than 0")
        else:
            self.length_min = new_length

    def set_year(self, new_year):
        if new_year <= 1400:
            print("Year must be after 1400")
        else:
            self.year = new_year

    def __str__(self):
        return (
            f"Play: {self.title}\n"
            f"Lead Actor: {self.lead_actor}\n"
            f"Length: {self.length_min} minutes\n"
            f"Year: {self.year}"
        )


# ------------------------------------------------------------
# PART 3 - Demo
# ------------------------------------------------------------

if __name__ == "__main__":

    actor1 = Actor("Tom Holland", 29, 68.0)
    actor2 = Actor("Tom Cruise", 63, 67.0)

    play1 = Play("Spiderman", actor1, 133, 2017)
    play2 = Play("Top Gun", actor2, 110, 1986)

    print(play1)
    print()
    print(play2)
    print()

    # Update an actor's age via setter and confirm the change is reflected.
    actor1.set_age(30)
    print(play1)

    # Trigger the validation warning with an invalid value.
    actor1.set_age(-5)
