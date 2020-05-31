

class Job:
    
    def __init__(self, title, link, date, id):
        '''
        This class holds job information and attributes
        '''
        
        self.title = title
        self.link = link
        self.date = date
        self.id = id
        self.applied = False
        self.old = False
        self.new = True
        self.desc = ''


