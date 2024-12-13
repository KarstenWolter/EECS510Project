def read_automaton(file_path):
    with open(file_path, 'r') as f:
        # Read states
        states = f.readline().strip().split()
        # Read input symbols
        input_symbols = f.readline().strip().split()
        # Read start state
        start_state = f.readline().strip()
        # Read accepting states
        accepting_states = set(f.readline().strip().split())
        
        # Read transitions
        transitions = {}
        
        for line in f:
            parts = line.strip().split()
            
            if len(parts) == 3:
                from_state, symbol, to_state = parts
            else:
                continue 

            if from_state not in transitions:
                transitions[from_state] = {}
            transitions[from_state][symbol] = to_state
        
    return states, input_symbols, start_state, accepting_states, transitions

def accept(automaton, w):
    states, input_symbols, start_state, accepting_states, transitions = automaton
    
    current_state = start_state
    transition_path = []
    
    for symbol in w:
        if current_state in transitions and symbol in transitions[current_state]:
            next_state = transitions[current_state][symbol]
            transition_path.append(f"{current_state} {symbol} {next_state}")
            current_state = next_state
        else:
            # No transition found, reject the string
            return "reject"
    
    # If the final state is accepting, accept the string
    if current_state in accepting_states:
        return "accept\n" + "\n".join(transition_path)
    else:
        return "reject"

automaton = read_automaton('automaton.txt')

# Test 1:
print(accept(automaton, ["dribble", "shotAttempt", "scored"]))  # Valid play 

# Test 2:
print(accept(automaton, ["dribble", "shotAttempt_miss_rebound", "shotAttempt" , "blocked"]))  # Valid play 

# Test 3:
print(accept(automaton, ["dribble", "pass"]))  # Invalid, needs an endPlayAction

# Test 4:
print(accept(automaton, ["dribble", "pass" , "pass" , "foul" , "twoMade"]))  # Valid play 


