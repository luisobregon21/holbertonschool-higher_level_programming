#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    best = None
    if a_dictionary is None:
        return None
    else:
        for student, grade in a_dictionary.items():
            if grade > score:
                score = grade
                best = student
        return best
