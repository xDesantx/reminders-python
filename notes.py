import json


class Notes:

    __notes={}


    def load(self):
        try:
            with open('save.sav', 'r') as file:
                return json.load(file)
        except:
            with open('save.sav', 'w') as file:
                return None
    def save(self):
        with open('save.sav','w') as file:
            json.dump(__notes, file)

    def addNew(self, note, time):
        self.__notes[note]=time
    
    #TODO delete func

    #TODO remind func

    def get_notes(self):
        return self.__notes


    def __init__(self):
        notes = self.load()


if __name__=='__main__':
    print('wrong file idot')