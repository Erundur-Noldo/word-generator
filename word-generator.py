#IT HAS BEEN MADE BY EMIKA



import sys
import random




#normalising the chances
def normalise_probabilities_structure(dictionary):
    total_chance = [0] * 3
    for sublist in dictionary.values():
        for i in range(3):
            total_chance[i] += sublist[i]
    for i in range(3):
        if(total_chance[i]) == 0:
            print("Error: you were about to divide by 0 because of the chances of your syllables or something")
            quit()
    
    normalised_dictionary = {}
    cumulative_prob = [0] * 3
    for key, sublist in dictionary.items():
        normalised_sublist = []
        for i in range(3):
            cumulative_prob[i] += sublist[i] / total_chance[i]
            normalised_sublist.append(cumulative_prob[i])
        normalised_dictionary[key] = normalised_sublist
    return normalised_dictionary
        
def normalise_probabilities_segment(dictionary): #best solution to a problem fr
    total_chance = sum(dictionary.values())
    if(total_chance) == 0:
        print("Error: you were about to divide by 0 because of the chances of your phonemes or something")
        quit()
    
    normalised_dictionary = {}
    cumulative_prob = 0
    for key, value in dictionary.items():
        cumulative_prob += value / total_chance
        normalised_dictionary[key] = cumulative_prob
    return normalised_dictionary
        
    
    
#generating a letter
def choose_letter(key):
    random_number = random.random()
    chosen_option = "Nonewait"
    
    if key in segments:
        for option, cumprob in segments[key].items():
            if (random_number <= cumprob):
                return (option)
    return (chosen_option)


        
def permitted_sequence(current_sequence):
    for forbidden_sequence in forbidden_sequences:
        if (forbidden_sequence in current_sequence): return False
    return True
    
def rewrite_sequence(sequence):
    for rewrite_sequence in rewrite_sequences:
        sequence = sequence.replace(rewrite_sequence[0], rewrite_sequence[1])
    return sequence

    
def generate_syllable(pos):
    #choosing one of the structures
    random_number = random.random()
    chosen_option = "Nonewait"
    for option, cum_prob in structures.items():
        if random_number <= cum_prob[pos]: #haha cum
            chosen_option = option
            break
    output = ""
    for key in chosen_option:
        output += choose_letter(key)
    return(output)




#initialisation~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

number = 1

# Check if the correct number of arguments are provided
if len(sys.argv) == 3:
    number = int(sys.argv[2])
elif len(sys.argv) != 2:
    print("that's not how you use this thing, pal\nusage: python3 word-generator.py <file_path> (<number of words>)")
    sys.exit(1)

# Get the file path from the command line argument
file_path = sys.argv[1]

# Attempt to store the file in a list
lines = []

try:
    with open(file_path, 'r') as file:
        # Read the entire contents of the file
        for line in file:
            if(line.strip() != ""):
                lines.append(line.strip())  # strip() to remove leading/trailing whitespace
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.\ncheck the name and the path and if you even made the file at all please thank you ^>^")
    quit()
except IOError as e: #I dunno what this even means I copypasted it
    print(f"(I don't know what this means but:)\nError: There was an IO error while trying to read the file '{file_path}': {e}")
    
    


    
#reading the file ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Initialize the dictionary to hold the segments
segments = {}
chances = {}
structures = {}
structure_chances = {}
forbidden_sequences = []
word_length = []
rewrite_sequences = []

#reading the chances of every character. it reads, and puts it in the dictionary with the chance attached to it
for line in lines:
    if line[0] == '#':
        pass #do nothing
    
    
    elif '>' in line and '~' in line:
        rest, last = line.split('~')
        if (last != ''): last = float(last.strip())
        else:            last = 0
        word_length = [float(part.strip().strip('~').strip()) for part in rest.split('>')]
        word_length.extend([last])
    
    
    elif '>' in line:
        sequence, rewrite = line.split('>')
        sequence = [part.strip() for part in sequence.split(',')]
        rewrite  = [part.strip() for part in rewrite .split(',')]
        if (len(rewrite) == 1) :
            rewrite_sequences.extend([[sequence[i], rewrite[0]] for i in range(len(sequence))])
        else:
            rewrite_sequences.extend([[sequence[i], rewrite[i]] for i in range(len(sequence))])
    
    
    elif '$' in line:
        structure, chance = [part.strip() for part in line.split(',')]
        parts = [part.strip() for part in chance.split('-')]
        # case: $a -> [a,a,a]
        if (len(parts) == 1): parts = [int(parts[0].strip('$'))] * 3
        elif (len(parts) == 2):
            # case: $a-b -> [a,b,b]
            if (parts[0].startswith('$')): parts = [int(parts[0].strip('$')), int(parts[1]), int(parts[1])]
            # case: a-b$ -> [a,a,b]
            else: parts = [int(parts[0]), int(parts[0]), int(parts[1].strip('$'))]
        # case: $a-b-c$ -> [a,b,c]
        elif (len(parts) == 3): 
            parts = [int(parts[0].strip('$')), int(parts[1]), int(parts[2].strip('$'))]
        else:
            print("Error: something seems to be wrong with your code?? the chances of the syllable structures seem to be wrong")
            quit()
        
        structures[structure] = parts
        
        
    elif line[0] == '!':
        forbidden_sequences.extend(part.strip('!').strip() for part in line.split(','))
        
        
    elif ',' in line and not ('=' in line):
        letter, chance = line.split(':')
        letter = [part.strip() for part in letter.split(',')]
        chance = [part.strip() for part in chance.split(',')]
        if (len(chance) == 1) :
            for i in range(len(letter)): chances[letter[i]] = int(chance[0])
        else:
            for i in range(len(letter)): chances[letter[i]] = int(chance[i])
        
#looking at all the categories, and putting every letter in the category in the dictionary, together with the chance that belongs to it
for line in lines:
    if '=' in line and not ('%' in line):
        key, values = [part.strip() for part in line.split('=')]
        values = {value.strip(): chances[value.strip()] for value in values.split(',')}
        segments[key] = values

#looking at the syllable structures
#for line in lines:


#normalising the probablities
structures = normalise_probabilities_structure(structures)
for key in segments:
    segments[key] = normalise_probabilities_segment(segments[key])
    
	

#generating the syllable~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



for i in range(0, number):
    output = ''
    current_length = 0

    #all but the last syllable
    while(random.random()*100.0 < word_length[min(current_length, len(word_length)-2)]):
        new_syllable = generate_syllable(min(current_length, 1))
        attempts = 0
        while (not permitted_sequence(output + new_syllable)): 
            new_syllable = generate_syllable(min(current_length, 1))
            if(attempts > 100):
                print("Error: your code friking sucks and it just kept trying to add a syllable and failing, so fix that please thank you ^>^")
                quit()
            else:   attempts += 1
        if(current_length > 100):
            print("Error: your code friking sucks and it just kept adding syllables, so either fix your code or just don't want 100 syllable long words please thank you ^>^")
            quit()
            
        output += new_syllable
        current_length += 1
    
    # the last syllable
    if (random.random() * 100.0 < word_length[-1]):
        new_syllable = generate_syllable(2)
        attempts = 0
        while (not permitted_sequence(output + new_syllable)): 
            new_syllable = generate_syllable(2)
            if(attempts > 100):
                print("Error: your code friking sucks and it just kept trying to add a syllable and failing, so fix that please thank you ^>^")
                quit()
            else: attempts += 1
        if(current_length > 100):
            print("Error: your code friking sucks and it just kept adding syllables, so either fix your code or just don't want 100 syllable long words please thank you ^>^")
            quit()
            
        output += new_syllable
        current_length += 1
        
    print(rewrite_sequence(output))
    
