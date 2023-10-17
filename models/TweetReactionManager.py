# Class that handles a TweetReaction list
class TweetReactionManager:
    def __init__(self):
        self.reactionList = []
        self.reaction = None

    def addReaction(self, reaction):
        self.reactionList.append(reaction)

    def checkTextForReaction(self, text) -> bool:
        for reaction in self.reactionList:
            if reaction.checkIfWordFit(text):
                self.reaction = reaction
                return True
        return False
