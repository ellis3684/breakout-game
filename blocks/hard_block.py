from .master_block import MasterBlock


class HardBlock(MasterBlock):
    def __init__(self):
        super().__init__()
        self.color('orange')
        self.points_given = 10
