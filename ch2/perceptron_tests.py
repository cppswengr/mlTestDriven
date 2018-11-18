import nose.tools as nt
import numpy as np

from perceptron import Perceptron


def no_training_data_supplied_test():
    the_perceptron = Perceptron()
    result = the_perceptron.predict()

    assert result == None, 'Should have no result with no training data.'

    # or this way, pick the one you like
    nt.assert_is_none(result, 'Should have no result with no training data.')


def train_an_OR_function_test():

    the_perceptron = Perceptron()

    the_perceptron.train([
                            [1, 1],
                            [0, 1],
                            [1, 0],
                            [0, 0],
                          ],
                          [1,1,1,0])

    nt.assert_equal(the_perceptron.predict([1, 1]), 1)
    nt.assert_equal(the_perceptron.predict([1, 0]), 1)
    nt.assert_equal(the_perceptron.predict([0, 1]), 1)
    nt.assert_equal(the_perceptron.predict([0, 0]), 0)


def detect_values_greater_than_five_test():
    the_perceptron = Perceptron()
    the_perceptron.train([
                            [ 5, -1],
                            [ 2, -1],
                            [ 0, -1],
                            [-2, -1],
                          ],
                          [1, 0, 0, 0])

    nt.assert_equal(the_perceptron.predict([8]),  1)
    nt.assert_equal(the_perceptron.predict([5]),  1)
    nt.assert_equal(the_perceptron.predict([2]),  0)
    nt.assert_equal(the_perceptron.predict([0]),  0)
    nt.assert_equal(the_perceptron.predict([-2]), 0)


def detect_a_complicated_example_test():

    # Create random variables
    n = 100

    inputs = list(map(list, zip(np.random.uniform(0, 100, n),
                                np.random.uniform(0, 100, n),
                                np.random.uniform(0, 100, n)
                               )
                      )
                  )

    labels = [int(x[0] +x[1] + x[2] < 150) for x in inputs]
    the_perceptron = Perceptron()
    the_perceptron.train(inputs, labels)

    n = 1000
    test_inputs = list(map(list, zip(np.random.uniform(0, 100, n),
                                     np.random.uniform(0, 100, n),
                                     np.random.uniform(0, 100, n)
                                    )
                           )
                       )

    test_labels = [int(x[0] + x[1] + x[2] < 150) for x in test_inputs]

    lti = len(test_inputs)
    ltl = len(test_labels)

    # Create separate test cases
    false_positives = 0
    true_positives = 0
    false_negatives = 0
    true_negatives = 0
    for input, label in zip(test_inputs, test_labels):
        prediction = the_perceptron.predict(input)
        if prediction == 1:
            if label == 1:
                true_positives += 1
            else:
                false_positives += 1
        else:
            if label == 0:
                true_negatives += 1
            else:
                false_negatives += 1

    # Make sure we generated as much data as we'd expect
    nt.assert_equal(false_positives + true_positives + true_negatives +
                        false_negatives, n)

    correctly_classified = true_positives + true_negatives
    print('correctly classified:', correctly_classified/n * 100, "%")
    assert correctly_classified > n * .9, \
        "Perceptron should be much better than random. {0} \
            correct".format(correctly_classified)



