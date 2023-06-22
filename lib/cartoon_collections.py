def roll_call_dwarves(dwarves):
    num = 0
    for num in range(len(dwarves)):
        print(f'{num + 1}. {dwarves[num]}')
        num += 1

def summon_captain_planet(planeteer_calls):
    return [f'{planeteer.capitalize()}!' for planeteer in planeteer_calls]

def long_planeteer_calls(words):
    for word in words:
        if len(word) > 4:
            return True
    return False

def find_the_cheese(items):
    cheeses = ["cheddar", "gouda", "camembert"]
    for cheese in cheeses:
        if cheese in items:
            return cheese
    return None
