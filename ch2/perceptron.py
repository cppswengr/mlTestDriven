class Perceptron:

    def train(self, inputs, labels):

        self._weights = [0.431, 0.02, 0.2]
        dummied_inputs = [x + [-1] for x in inputs]

        for _ in range(4):

            for input, label in zip(dummied_inputs, labels):
                label_delta = (label - self.predict(input))

                for index, x in enumerate(input):
                    self._weights[index] += .1 * x * label_delta

    def predict(self, input=[]):

        if len(input) == 0:
            return None

        input = input + [-1]
        return int(0 < self._weights[0] * input[0] + self._weights[1] * input[1])

        # weight_input_pairings = zip(self._weights, input)
        # weight_input_products = [x[0]*x[1] for x in weight_input_pairings]

        # return int(0 < sum(weight_input_products))

