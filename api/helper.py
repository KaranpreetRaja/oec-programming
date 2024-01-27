
import random


def create_session(level, amount):
    # Create a session given level and amount of prompts
    # Returns a session_id and a list of prompts
    selections = []
    for i in range(amount):
        if level == 1:
            # select random shape from shapes
            selections.append(random.choice(shapes))
        elif level == 2:
            # select random shape from shapes
            random_entry = lambda x: x[random.randrange(len(x))]
            selections.append(" ".join([random_entry(nouns), random_entry(verbs), random_entry(adv), random_entry(adj)]))