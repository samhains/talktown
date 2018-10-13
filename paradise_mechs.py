import code
import tracery
import random
from tracery.modifiers import base_english


def encounter_person(person, other, activity):
    """Outline the unidirectional relationships between these two."""
    if other not in person.relationships or random.random() > 0.8:
        evade_text(person.name, other.name)
    else:
        other.life_events
        other.basic_appearance_description
        other.year_i_moved_here()

        relationship_dict = person.relationships[other].relationship_dict()
        encounter_text(person.name, other.name, activity, relationship_dict)

def return_character_social_network(sim, person):
    """Print out a character's relationships to everyone else in the town."""
    others = []
    for resident in sim.town.residents:
        if person.relation_to_me(resident) is not None:
            others.append(resident)

    return others



def setup_tracery(rules):
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    return grammar.flatten("#origin#")

def evade_text(name, other):
    rules = {
        'name' : name,
        'other': other,
        'origin': ['#alert#.#luck#', "#name# slidees right past #other# - Perhaps they don't know eachother?"],
        'alert': ["#name# hears somebody emerging from the #thing#"],
        'thing': ["subterranean mech layer", "carbon latch", "polishing unit"],
        'luck': ["Fortunately for #name#, they have never met #other# before so they are able to continue towards their task."]

    }
    print setup_tracery(rules)

def wakeup_text(name, activity):
    rules = {
        'name' : name,
        'activity': activity,
        'origin': ['#name# gets up and wanders to a late morning #activity#.'],
    }
    print setup_tracery(rules)

def encounter_text(name, other, activity, relationship_info):
    rules = {
        'name' : name,
        'activity': activity,
        'other': other,
        'origin': ['Unfortunately, as #name# attempts to go to the hotel #activity#, they encounter #other# #otherActivity#.'],
        'otherActivity': ["standing by the oil cooler.", "waiting for them by the escalator"]
    }
    print setup_tracery(rules)


def play(sim):
     # prints, e.g., "Hello, world!"
    activity = random.choice(['volley ball', 'table tennis', 'dosage of TeknoLust', 'SkyRide', 'spa carnival', 'Water Works', 'Serenity Adult-Only retreat'])

    print("Welcome to Mech Paradise Mechs")
    unrequited_love_cases = sim.story_recognizer.unrequited_love_cases
    person = unrequited_love_cases[0].nonreciprocator
    print("Today we will be following the life of Mech, {}, {}.".format(person.name, person.description))
    wakeup_text(person.name, activity)

    others = return_character_social_network(sim, person)

    for other in others[:5]:
        encounter_person(person, other, activity)

