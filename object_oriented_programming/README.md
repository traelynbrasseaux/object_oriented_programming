# OOP — Actors and Plays

The first object-oriented programming assignment: building two classes (`Actor` and `Play`) that demonstrate the basics of Python OOP — attributes, getters and setters with validation, composition, and `__str__`.

## What this assignment covers

- Defining a class with `__init__` and instance attributes
- Writing **getter** methods (`get_name`, `get_age`, …) and **setter** methods (`set_name`, `set_age`, …)
- Adding **validation** inside setters (reject negative ages, non-positive heights, runtimes ≤ 0, and years before 1400) and printing a warning instead of updating
- **Composition** — a `Play` holds an `Actor` object as its `lead_actor`
- Implementing `__str__` so `print(obj)` produces human-readable output
- Using the `if __name__ == "__main__":` idiom to keep demo code separate from class definitions

## What's in the file

- **`Actor`** — fields: `name` (str), `age` (int), `height` (float). Setters validate age and height before assigning.
- **`Play`** — fields: `title`, `lead_actor` (an `Actor`), `length_min`, `year`. Setters validate `length_min > 0` and `year >= 1400`. Its `__str__` includes the lead actor's info, demonstrating that printing a composed object cascades through to the inner object's `__str__`.

The main block demonstrates the full lifecycle: creating two actors, building two plays around them, printing each play, updating an attribute via a setter and reprinting, and triggering the validation warning by attempting an invalid update.

## How to run

```bash
python assignment.py
```

## Notes

The assignment description lives in [`ASSIGNMENT.md`](ASSIGNMENT.md). No external dependencies — pure standard-library Python 3.

This assignment is the prerequisite for the **Inheritance — Performers and Productions** project, which generalizes `Actor` into a `Performer` base class with three specialized subclasses.
