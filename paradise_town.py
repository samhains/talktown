import code
import tracery
import random
from tracery.modifiers import base_english

energy_levels = 5
unfavourables = []
favourables = []

def return_character_social_network(sim, person):
    """Print out a character's relationships to everyone else in the town."""
    others = []
    for resident in sim.town.residents:
        if person.relation_to_me(resident) is not None:
            others.append(resident)

    return others



def setup_tracery(rules, origin="#origin#"):
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    return grammar.flatten(origin)

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
        'wanders': ['wanders', 'walks', 'meanders', 'moves', 'trundles', 'hops over to'],
        'sleeping_area': ['sleeping chamber', 'oxygen room', 'REM chamber', 'bed', 'sleeping quarters'],
        'wakes': ['wakes up', 'wipes their eyeballs', '#rolls# out of their #sleeping_area#'],
        'rolls': ['slides', 'flops', 'slips', 'bounces', 'pops'],
        'origin': ['#name# #wakes# and #wanders# to #activity#.'],
    }
    print setup_tracery(rules)

def weather_statement(person):
    weather = random.choice(["good", "bad"])
    print("{} looks up. It seems like the weather is {}, today.".format(person.name, weather))

def extended_family_question(person):

    family_member = random.choice(list(person.extended_family))
    relation = person.relation_to_me(family_member)
    life_event = str(family_member.life_events[-1])

    if len(family_member.occupations) >0:
        occupations = [str(occupation) for occupation in family_member.occupations]
    else:
        occupations = ['Unemployed']

    rules = {
        'name' : person.name,
        'origin': ['#question#\n#response#\n#goodbye#'],
        'family': family_member.name,
        'occupations': occupations,
        'relation': relation,
        'fine': ['good', 'healthy', 'in good health', 'fine'],
        'lifeEvent': life_event,
        'goodbye': ['Fairwell.', 'So long.', 'Goodbye'],
        'question': ['How is your #relation#, #family#? Are they still #occupations#?'],
        'response': ['They are #fine#, they are mostly concerned with the #lifeEvent#']
    }
    print setup_tracery(rules)

def encounter_text(person, other, activity):
    relation = person.relation_to_me(other)

    rules = {
        'name': person.name,
        'activity': activity,
        'relation': relation,
        'other': other.name,
        'origin': ['#unfortunately#, as #name# #attempts# to go to the #activity#, they #encounter# their #relation# #other# #otherActivity#.'],
        'encounter': ['encounter', 'bump into', 'catch sight of', 'catch a glimpse of', 'hear', 'see'],
        'attempts': ['attempts', 'tries', 'continues'],
        'unfortunately' : ['Unfortunately', 'Sadly', 'Annoyingly', 'Irritatingly'],
        'cooler': ['cooler', 'escalator', 'house cat', 'ship wreck', 'pile of waste', 'cyber booth'],
        'otherActivity': ["appearing as a nearby #hologram#","standing by the #material# #cooler#.", "waiting for them by the escalator"],
        'material': ['oil', 'diamond', 'sulphur', 'toxin', 'machine-gun', 'lamentation', 'auburn', 'binary'],
        'hologram': ['hologram', 'ghost', 'apparition', 'time wasting activity', 'mental feeling']
    }
    print setup_tracery(rules)

def random_memory_text(person, life_event):
    rules = {
        'name': person.name,
        'lifeEvent': str(life_event).lower(),
        'suddenly': ['All of a sudden', 'immediately', 'instantaneously', 'Instantly', 'Straightaway', 'All at once', 'Promptly', 'Abruptly'],
        'memory': ['thought', 'vision', 'apparition', 'intense feeling', 'recollection'],
        'remember': ['recollect', 'consider', 'recall', 'remember'],
        'origin': ['#suddenly#, #memory.a# occurred to #name# - They #remember# the #lifeEvent#.'],
    }
    print setup_tracery(rules)

def random_memory(person):
    life_events = person.life_events
    if len(life_events) > 0:
        life_event = random.choice(life_events)
        random_memory_text(person, life_event)



def love_interest_question_text(person, other, companies):
    rules = {
        'name': person.name,
        'other': other.name,
        'origin': ['#question#'],
        'intimate': ['intimate', 'warm', 'close', 'long'],
        'event': companies,
        'take': ['take', 'ride', 'accompany', 'follow'],
        'interested': ['interested in', 'curious about', 'lusting for', 'wishing for', 'crushing on'],
        'intoYou': ['want to #take# you to #event#', 'have #intimate# conversations with you', 'spend #intimate# evenings with you'],
        'gender': ['boys', 'girls', 'men', 'women', 'boys and girls', 'bodies', 'flesh'],
        'question': ["Who are you #interested#, #name#?", "Is there someone that you are #interested#, #name#?",
                          "I bet there are a lot of automaton #gender# that would #intoYou#, #name#. Are you #interested# anyone?"]
    }
    print setup_tracery(rules)

def calc_spark_level(person, other):
    return person.relationships[other].spark

def love_interest_statement_text(person, other):
    spark_level = calc_spark_level(person, other)
    rules = {
        'name': person.name,
        'other': other.name,
        'occupation': ['bartender'],
        'spark': spark_level,
        'origin': ['I heard you are into #other# the #occupation#, I heard your spark levels were around #spark#']
    }
    print setup_tracery(rules)

def love_interest_response_text(person, other):
    rules = {
        'name': person.name,
        'other': other.name,
        'origin': ['#question#'],
        'intimate': ['intimate', 'warm', 'close', 'long'],
        'take': ['take', 'ride', 'accompany', 'follow'],
        'interested': ['interested in', 'curious about', 'lusting for', 'wishing for', 'crushing on'],
        'intoYou': ['want to #take# you to #event#', 'have #intimate# conversations with you', 'spend #intimate# evenings with you'],
        'gender': ['boys', 'girls', 'men', 'theys', 'women', 'boys and girls', 'bodies', 'flesh'],
        'question': ["Who are you #interested#, #name#?", "Is there someone that you are #interested#, #name#?",
                     "I bet there are a lot of automaton #gender# that would #intoYou#, #name#. Are you #interested# anyone?"]
    }
    print setup_tracery(rules)

def love_interest_text(person, other, companies, love_interests):

    company_names = [company.name for company in companies]
    rules = {
    'name' : person.name,
    'other': other.name,
    }

    love_interest_question_text(person, other, company_names)

    if len(love_interests) > 0:
        love_interest = random.choice(list(love_interests))
        #print('love interest text', love_interest)
        #love_interest_statement_text(person, love_interest)

    # if other.name not in person.relationships:
    #     pass
    # else:
    #     print person.relationships[other.name].outline()

    # if len(love_interests) > 0:
    #     love_interest = random.choice(love_interests)
    #     print("\"You know who I'm interested in, {}. {}, of course!\" said {}".format(other.name, love_interest.name, person.name ))
    # else:
    #     love_interest_of_other = love_interests_of_other[0]
    #     print("\"Nobody. But I know that you're interested in {} the {}".format(love_interest_of_other.name, love_interest_of_other.occupations[0]))

def collapse_text(person):
    rules = {
        'name': person.name,
        'suddenly': ['All of a sudden', 'immediately', 'instantaneously', 'Instantly', 'Straightaway', 'All at once', 'Promptly', 'Abruptly'],
        'origin': ['#suddenly#, #name# collapses on the floor.'],
    }
    print setup_tracery(rules)

def encounter_person(person, other, activity, companies, love_interests):
    """Outline the unidirectional relationships between these two."""
    global energy_levels
    # print("energy",energy_levels)
    # print(other.name)
    # print("is captivated by", other.is_captivated_by)


    encounter_text(person, other, activity)
    love_interest_text(person, other, companies, love_interests)
    random_memory(person)
    extended_family_question(person)
    weather_statement(person)
    energy_levels = energy_levels - 1


    # print("other love interest is captivated by", other.is_captivated_by[-1].is_captivated_by)

    # if person.likes(other) and other.likes(person):
    #     favourables.append(person)
    #     print("friendship encounter")
    #     energy_levels += 1
    #
    # elif person.likes(other) and not other.likes(person):
    #     unfavourables.append(person)
    #     energy_levels -= 1
    #     print("rejection text")
    #
    # elif not person.likes(other) and other.likes(person):
    #     unfavourables.append(person)
    #     print("attempt to avoid text")
    #     if random.random() > 0.5:
    #         print("successfully avoid text")
    #     else:
    #         energy_levels -= 1
    #         print("failure to avoid text")
    # else:
    #     if random.random > 0.7:
    #         energy_levels -= 1;
    #         print("bump into stranger text")
    #     else:
    #         print("both avoid text")

    # print(other.basic_appearance_description)
    # for event in other.life_events:
    #     print(event)

    # if other not in person.relationships or random.random() > 0.8:
    #     evade_text(person.name, other.name)
    # else:
    #     other.life_events
    #     other.basic_appearance_description
    #     other.year_i_moved_here()
    #
    #     relationship_dict = person.relationships[other].relationship_dict()
    #     encounter_text(person.name, other.name, activity, relationship_dict)
def cheesy_single_text(person):
    rules = {
        'name' : person.name,
        'origin': ["#name# #recently# single, and is ready to #explore#.", '#name# #recently# single.',
                   '#name# is single.'],
        'explore': ['explore', 'mingle', 'search', 'find love', 'find companionship'],
        'recently': ['is recently', 'has just become', 'has just bust onto the scene as a', 'is',
                     'has always been', 'a #mournful#', 'is #happily#' ],
        'happily': ['happily', 'fortunately', 'merrily', 'joyfully', 'spiritedly', 'jovial'],
        'mournful': ['lonely', 'mournful', 'unfortunately','crestfallen', 'depressive']
    }

    print setup_tracery(rules)

def long_description(person):
    print("{}, {} from {}.".format(person.name, person.description, person.home.block))

def crush_metrics_text(person, other):
    person_spark_for_them = person.relationships[other].spark
    their_spark_for_person= other.relationships[person].spark
    person_name = person.name
    other_name = other.name

    print("{} spark levels are at around {}, while {} spark levels are at around {}.".format(
        person_name, person_spark_for_them, other_name, their_spark_for_person))
    if person_spark_for_them >= 15 and their_spark_for_person >= 15:
        print("They are both into eachother.")
    elif person_spark_for_them < 15 and their_spark_for_person < 15:
        print("Neither of them are into eachother.")
    elif person_spark_for_them >= 15 and their_spark_for_person <15:
        print("{} is way more into {}".format(person_name, other_name))
    else:
        print("{} is way more into {}".format(other_name, person_name))




def love_life_summary(person, spouse, love_interests):
    if person.spouse:
        spouse_name = spouse.name
        print("{}, has a partner and their name is {}.".format(person.name, spouse_name))
        long_description(spouse)
        crush_metrics_text(person, spouse)
    else:
        cheesy_single_text(person)
        if len(love_interests) > 0:
            love_interest = love_interests[0]
            print(love_interest.name)
            print("{} most intense love interest is {}.".format(person.name, love_interest.name))
            long_description(love_interest)
            crush_metrics_text(person, love_interest)



def play(sim):
    print(sim.town.dwelling_places)
    location_names = sim.town.companies
    location_names = [location_name.name for location_name in location_names]

    activity = random.choice(location_names)
    # look for work
    # depart town
    # find person of certain ocupation
    #socialize
    companies = sim.town.companies
    print("Welcome to Paradise Town")
    print("The worlds longest running automated Reality Television series")
    unrequited_love_cases = sim.story_recognizer.unrequited_love_cases

    person = unrequited_love_cases[0].nonreciprocator
    spouse = person.spouse
    other_love_interests = sorted(person.is_captivated_by, key=lambda li: person.relationships[li].spark, reverse=True)

    print("Today we will be following the life of automaton, {}, {}.".format(person.name, person.description))
    love_life_summary(person, spouse, other_love_interests)

    wakeup_text(person.name, activity)

    others = return_character_social_network(sim, person)

    global energy_levels
    for other in others:
        if energy_levels > 0:
            encounter_person(person, other, activity, companies, other_love_interests)
        else:
            collapse_text(person)
            break


