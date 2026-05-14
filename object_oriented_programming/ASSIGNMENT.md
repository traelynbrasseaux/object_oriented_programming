# OOP Assignment: Actors and Plays

## Overview

In this assignment, you will practice **Object-Oriented Programming (OOP)** in Python by building two classes: `Actor` and `Play`. You will define attributes, write getter/setter methods, and connect the two classes together.

Work through each section in `assignment.py`. Read all instructions carefully before writing any code.

---

## Background: What is a Class?

A **class** is like a blueprint for creating objects. For example, every actor has a name, an age, and a height — but each specific actor has their own values for those attributes.

```python
# This is what a class looks like at a high level:
class Actor:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
```

---

## Part 1 — The Actor Class

Build an `Actor` class with the following attributes:

| Attribute | Type   | Description                          |
|-----------|--------|--------------------------------------|
| `name`    | `str`  | The actor's full name                |
| `age`     | `int`  | The actor's age in years             |
| `height`  | `float`| The actor's height in inches         |

### Requirements

- Define an `__init__` method that takes `name`, `age`, and `height` as parameters.
- Write a **getter** method for each attribute (e.g., `get_name()`).
- Write a **setter** method for each attribute (e.g., `set_name(new_name)`).
  - The setter for `age` should **reject negative values** and print a warning instead of updating.
  - The setter for `height` should **reject values of 0 or below** and print a warning instead of updating.
- Write a `__str__` method that returns a readable string describing the actor.

### Example Output

```
Actor: Viola Davis | Age: 58 | Height: 63.0 in
```

---

## Part 2 — The Play Class

Build a `Play` class with the following attributes:

| Attribute      | Type    | Description                            |
|----------------|---------|----------------------------------------|
| `title`        | `str`   | The name of the play                   |
| `lead_actor`   | `Actor` | An Actor object (from Part 1)          |
| `length_min`   | `int`   | Runtime of the play in minutes         |
| `year`         | `int`   | Year the play was written or premiered |

### Requirements

- Define an `__init__` method that accepts all four attributes above.
- Write getter and setter methods for each attribute.
  - The setter for `length_min` should reject values less than or equal to 0.
  - The setter for `year` should reject values before 1400 (the earliest known plays).
- Write a `__str__` method that returns a readable multi-line summary of the play, including the lead actor's info.

### Example Output

```
Play: Fences
Lead Actor: Viola Davis | Age: 58 | Height: 63.0 in
Length: 150 minutes
Year: 1985
```

---

## Part 3 — Putting It Together

Once both classes are working, do the following in the `if __name__ == "__main__":` block at the bottom of `assignment.py`:

1. Create **two Actor objects** of your choice (real or fictional).
2. Create **two Play objects**, each using one of your actors as the lead.
3. Print both plays using `print()`.
4. Use a setter to update one actor's age, then print the play again to confirm the change is reflected.
5. Try to set an invalid value (e.g., a negative age) and confirm your validation prints a warning.

---

## Stretch Goals (Optional)

These are not required, but try them if you finish early:

- Add a `supporting_cast` attribute to `Play` that holds a **list** of `Actor` objects.
- Write an `add_actor(actor)` method that appends to that list.
- Write a method `list_cast()` that prints the names of all actors in the supporting cast.
- Add a `get_runtime_hours()` method to `Play` that converts `length_min` to hours and minutes and returns a formatted string like `"2 hours, 30 minutes"`.

---

## Submission

When you are done:

1. Save your file.
2. Run it and make sure there are no errors.
3. Commit your changes with a meaningful message:

```bash
git add assignment.py
git commit -m "Complete OOP Actor and Play assignment"
git push
```

Good luck!
