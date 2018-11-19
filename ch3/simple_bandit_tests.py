from nose.tools import assert_equal

import simple_bandit


def given_a_single_treatment_test():
    bandit = simple_bandit.SimpleBandit(['A'])
    chosen_treatment = bandit.choose_treatment()
    assert_equal(chosen_treatment, 'A', 'Should choose the '
                                        'only available option.')


def given_two_treatments_and_no_payoffs_test():
    treatments = ['A', 'B']
    bandit = simple_bandit.SimpleBandit(treatments)
    chosen_treatment = bandit.choose_treatment()
    assert_equal(chosen_treatment, treatments[0], 'Should choose the '
                                                  'first treatment to start')


def given_two_treatments_test():
    treatments = ['A', 'B']
    bandit = simple_bandit.SimpleBandit(treatments)
    treatments_chosen = []

    for i in range(5):
        chosen_treatment = bandit.choose_treatment()
        treatments_chosen.append(chosen_treatment)
        bandit.log_payout(chosen_treatment, 0.00)
    assert_equal(treatments_chosen.count('A'), 5, 'Should explore treatment A '
                                                 'for the first 5 tries')

    for i in range(5):
        chosen_treatment = bandit.choose_treatment()
        treatments_chosen.append(chosen_treatment)
        bandit.log_payout(chosen_treatment, 5.00)
    assert_equal(treatments_chosen.count('B'), 5, 'Should explore treatment B '
                                                  'for the second 5 tries')
    for i in range(5):
        chosen_treatment = bandit.choose_treatment()
        treatments_chosen.append(chosen_treatment)
    assert_equal(treatments_chosen.count('B'), 10, 'Should explore treatment B '
                                                  'for the next 5 tries after'
                                                   ' exploring - "exploiting"')
    # make sure we return to exploring
    for i in range(5):
        chosen_treatment = bandit.choose_treatment()
        treatments_chosen.append(chosen_treatment)
        bandit.log_payout(chosen_treatment, 0.00)
    assert_equal(treatments_chosen.count('A'), 10, 'Should explore treatment A '
                                                  'for the next 5 tries')

    # make sure the pattern is being followed, i.e., A then B
    for i in range(5):
        chosen_treatment = bandit.choose_treatment()
        treatments_chosen.append(chosen_treatment)
        bandit.log_payout(chosen_treatment, 5.00)
    assert_equal(treatments_chosen.count('B'), 15, 'Should explore treatment B '
                                                  'for the next 5 tries')

    # ensure the last step in  the pattern is followed
    for i in range(5):
        chosen_treatment = bandit.choose_treatment()
        treatments_chosen.append(chosen_treatment)
    assert_equal(treatments_chosen.count('B'), 20, 'Should explore treatment B '
                                                   'for the next 5 tries after'
                                                   ' exploring - "exploiting"')

    # make sure we return to exploring
    for i in range(5):
        chosen_treatment = bandit.choose_treatment()
        treatments_chosen.append(chosen_treatment)
        bandit.log_payout(chosen_treatment, 0.00)
    assert_equal(treatments_chosen.count('A'), 15, 'Should explore treatment A '
                                                  'for the next 5 tries')
