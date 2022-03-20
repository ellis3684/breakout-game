from .master_block import MasterBlock


class MediumBlock(MasterBlock):
    def __init__(self):
        super().__init__()
        self.color('yellow')
        self.points_given = 5
