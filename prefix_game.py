import random


class prefix_game:

    def __init__(self):
        self.total_score = 0
        self.num_rounds = 0
        self.word_list = ["inject", "project", "predict", "contradict", "indict", "resume",
                          "presume", "consume", "concept", "except", "contracept", "conclude", "exclude", "preclude"]
        self.pre_suff_list = mydict = [{"base": "ject", "prefix": ["in", "pro", "out", "pre", "con"]}, {"base": "dict", "prefix": ["pre", "contra", "pro", "con", "in"]}, {"base": "sume", "prefix": [
            "re", "con", "contra", "pro", "in"]}, {"base": "cept", "prefix": ["con", "ex", "contra", "in", "out"]}, {"base": "clude", "prefix": ["con", "ex", "pre", "pro", "contra"]}]
        self.current_round_score = 0
        self.current_prefix_set = {}
        self.current_base = "UNDEFINED"

    def draw_prefixes(self):
        return random.choice(self.pre_suff_list)

    def get_score(self):
        return self.total_score

    def get_current_round_score(self):
        return self.current_round_score

    def update_score(self, reward):
        self.current_round_score = self.current_round_score + reward
        self.total_score = self.total_score + reward

    def is_correct(self, word):
        return (word in self.word_list)

    def next_round(self):
        self.num_rounds = self.num_rounds + 1
        self.current_round_score = 0
        self.current_prefix_set = self.prefix_list[:5]  # choose randomly
        self.current_base = self.base_list[0]  # choose randomly

    def reset(self):
        self.total_score = 0
        self.num_rounds = 0
