from random import sample, shuffle, choice


class Task:
    def __init__(self, *words):
        """
        the first one is a question
        """
        self.quest = words[0]
        self.words = sample(words, len(words))
        self.eng = choice((True, False))
        shuffle(self.words)

    def question(self):
        return '🇬🇧 ' + self.quest.eng if self.eng else '🇷🇸 ' + self.quest.srb

    def options(self):
        return ['🇷🇸 ' + word.srb for word in self.words] if self.eng else ['🇬🇧 ' + word.eng for word in self.words]

    def correct(self):
        return self.words.index(self.quest)
