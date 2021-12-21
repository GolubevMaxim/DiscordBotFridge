class ReactionRoles:
    def __init__(self, message_id, reactions, roles):
        self.message_id = message_id
        self.reactions = reactions
        self.roles = roles

    def get_role_by_reaction(self, reaction):
        return self.roles[self.reactions.index(reaction)]