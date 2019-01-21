import random

def randomize(message=""):
    """Return random integer between specified
    Expected format: !random {} to {}
    Other format: !random (will return between 1 and 100)
    """
    random_format = "-\nIncorrect format\n" + \
                "use `!random a to b`\n" + \
                "where a and b are numbers and a < b"
                
    gen = message.content.split()

    if len(gen) == 1:
        return random.randint(1,100)
    if len(gen) < 4:
        return random_format

    try:
        a = int(gen[1])
        b = int(gen[3])
    except ValueError:
        return random_format
            
    if gen[2] != "to" or a > b:
        return random_format

    return f'`{random.randint(a,b)}`'