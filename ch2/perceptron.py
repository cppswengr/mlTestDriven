class Perceptron:

    def train(self, inputs, labels):

        dummied_inputs = [x + [-1] for x in inputs]
        self._weights = [0.2] * len(dummied_inputs[0])

        for _ in range(6000):

            for input, label in zip(dummied_inputs, labels):
                prediction = self.predict(input)
                label_delta = (label - prediction)
                # label_delta = (label - self.predict(input))

                for index, x in enumerate(input):
                    self._weights[index] += .1 * x * label_delta

    def predict(self, input=[]):

        if len(input) == 0:
            return None

        input = input + [-1]
        return int(0 < sum([x[0] * x[1] for x in zip(self._weights, input)]))

        # return int(0 < self._weights[0] * input[0] + self._weights[1] * input[1])

        # weight_input_pairings = zip(self._weights, input)
        # weight_input_products = [x[0]*x[1] for x in weight_input_pairings]

        # return int(0 < sum(weight_input_products))

