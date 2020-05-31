

class Job:
    
    def __init__(self, title, link, date, job_id):
        '''
        This class holds job information and attributes
        '''
        
        self.title = title
        self.link = link
        self.date = date
        self.job_id = job_id
        self.applied = False
        self.old = False
        self.new = True
        self.desc = ''


