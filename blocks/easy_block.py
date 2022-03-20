from .master_block import MasterBlock


class EasyBlock(MasterBlock):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.points_given = 1
