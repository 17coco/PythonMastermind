'''
    class Row
'''
class Row:
    '''class of a row of Marble obejcts'''
    def __init__(self, list_of_marbles):
        self.marbles = list_of_marbles

    def get_marble(self, index):
        '''get the marble according to the index'''
        return self.marbles[index]
    
    def mass_erase(self):
        '''erase all marbles of this row'''
        for each in self.marbles:
            each.erase()
            
    def reset_panel(self, colors = ["red", "blue", "green",
                                    "yellow", "purple", "black"]):
        '''reset all marbles of this row to white'''
        for index, value in enumerate(self.marbles):
            self.marbles[index].set_color(colors[index])
        # update color
        for each in self.marbles:
            each.draw()
