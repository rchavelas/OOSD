class SdModel:
    ''' 
    
    This class helps build Systems Dynamics models in Python 
    
    It complies with the XMILE standard

    '''

    def __init__(self, name, start=None, stop=None, dt=None, 
                 save_step=None, time_units=None):
        self.name = name
        self.start = start
        self.stop = stop
        self.dt = dt
        self.time_units = time_units
        self.stocks = {}
        self.flows = {}
        self.auxiliaries = {}
        self.tables = {}

    def add_stock(self, name, eqn, units=None, 
                  inflow=None, outflow=None, biflow=None,
                  non_negative=True):
        pass

    def add_flow(self, name, eqn, units=None, non_negative=True):
        pass

    def add_auxiliary(self, name, eqn, units=None, gf=None):
        pass

    def add_table(self):
        pass
