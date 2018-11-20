from simple_bandit import SimpleBandit
from scenarios import BanditScenario
import numpy as np
import matplotlib.pyplot as plt

simulated_experiment = BanditScenario({
    'A': {
       'conversion_rate': .05,
       'order_average': 35.00
    },
    'B':{
        'conversion_rate': .06,
        'order_average': 36.00
    }
})


simple_bandit = SimpleBandit(['A', 'B'])

for visitor_i in range(500):
    treatment = simple_bandit.choose_treatment()
    payout = simulated_experiment.next_visitor(treatment)
    simple_bandit.log_payout(treatment, payout)

plt.title('Money made by different stategies')
plt.xlabel('Visitor #')
plt.ylabel('Total $ made')

plt.title('Money made by different stategies')
plt.xlabel('Visitor #')
plt.ylabel('Total $ made')

plt.plot(np.array(simulated_experiment._bandit_payoffs).
         cumsum(), label='Bandit')

plt.plot(np.array(simulated_experiment._scenario_payoffs['B']).
         cumsum(), label='Treatment B')

plt.plot(np.array(simulated_experiment._scenario_payoffs['A']).
         cumsum(), label='Treatment A')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()