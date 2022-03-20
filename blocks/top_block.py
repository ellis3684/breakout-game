from .master_block import MasterBlock


class TopBlock(MasterBlock):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.points_given = 25
