import numpy as np


class BanditScenario:

    def __init__(self, scenario):
        self._scenario = scenario
        self._scenario_payoffs = \
            {treatment_name:[] for treatment_name in self._scenario.keys()}
        self._bandit_payoffs = []

    def next_visitor(self, treatment):
        for key, value in self._scenario.items():
            ordered = np.random.binomial(1, value['conversion_rate'])
            order_average = np.random.normal(loc=value['order_average'], scale=5.00)
            self._scenario_payoffs[key].append(ordered*order_average)
            if key == treatment:
                self._bandit_payoffs.append(ordered*order_average)

        # retval =  self._scenario_payoffs[treatment][-1]
        return self._scenario_payoffs[treatment][-1]
