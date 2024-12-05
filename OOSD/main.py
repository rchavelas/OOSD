class SdModel:
    ''' This class helps build Systems Dynamics models in Python '''

    def __init__(self, name, start, end, dt, save_step, time_units):
        self.name = name
        self.start = start
        self.end = end
        self.dt = dt
        self.save_step = save_step
        self.time_units = time_units
        self.stocks = {}
        self.flows = {}
        self.auxiliaries = {}
        self.tables = {}

    def add_stock(self, name, initial,  units, 
                  inflow, outflow, biflow):
        pass

    def add_flow(self, name, equation):
        pass

    def add_auxiliary(self, name, equation, units):
        pass

    def add_table(self):
        pass



#carta de intención + curriculum vitae