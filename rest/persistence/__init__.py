class PersistenceLayer(object) :
    def save_system(self, system):
        raise NotImplementedError
    
    def funcname(self, parameter_list):
        raise NotImplementedError


class DaoFactory:
    @staticmethod
    def get_instace():
        pass