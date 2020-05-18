class calculation():

    def __init__(self, data):
        self.data = data

    def maxs(self, col_name):
        print('max values:  \n', self.data[col_name].max())
        print('\n')

    def mins(self, col_name):
        print('min values: \n', self.data[ col_name ].min())
        print('\n')

    def means(self, col_name):
        print('mean values: \n \n', self.data[ col_name ].mean())
        print('\n')

    def summ(self, col_name):
        print('sums are: \n \n', self.data[ col_name ].sum())
        print('\n')