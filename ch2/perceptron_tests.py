import nose.tools as nt

from perceptron import Perceptron


def no_training_data_supplied_test():
    the_perceptron = Perceptron()
    result = the_perceptron.predict()

    assert result == None, 'Should have no result with no training data.'

    # or this way, pick the one you like
    nt.assert_is_none(result, 'Should have no result with no training data.')
