class FiniteAutomata:
    def __init__(self, n_states, state_symbol="q", ip_alphabet, delta):
        """
        Forms the basics of all FA machines.
        
        Keyword arguments:
          1) n_states     -- number of states in FA.
          2) state_symbol -- alphabet used to define each state. 
                             For eg: q,   where, states will be q0, q1, q2, q3, ...
          3) ip_alphabet  -- set of input symbols.
          4) delta        -- transition function.
        
        """
        
        # user entered variables.
        self.n_states = n_states
        self.ip_symbol = ip_symbol
        self.delta = delta
        
        # derived variables.
        self.states = [state_symbol + str(i) for i in range(n_states)]
        self.start_state = 
        
    def step(self, ip):
        
