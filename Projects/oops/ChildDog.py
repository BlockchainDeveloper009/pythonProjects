import ParentDog;
class ChildDog(ParentDog):

    def __init__(self, name):
        self.charac = []

    def add_trick_char(self, trick, characterAttr):
        self.add_trick(self, trick)
        self.charac.append(characterAttr)