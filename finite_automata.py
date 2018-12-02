class FiniteAutomata(object):

    def __init__(self, delta, initial_state = 'q0', final_state="qf", sigma=None):
        """
            delta{ 
                data_type = 'nested dictionary',
                output    : 'next_state',
                input     : state, input
                example   : delta[state, input] --> next_state
            }
        """
        self.delta = delta
        self.initial_state = initial_state
        self.current_state = initial_state
        self.init_missing()

    def init_missing(self):
        if self.sigma is None:
            self.sigma = list(self.compute_sigma())
        return self.delta.keys()

a = FiniteAutomata({1:1, 2:2})
