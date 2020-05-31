from Companies import Intel
from Companies import Microchip

class Manager:
    '''
    This class manages all the job listings by company
    '''

    def __init__(self):
        self.company_dict = {
            'intel':Intel('intel', 'https://jobs.intel.com/ListJobs/All/Search/jobtitle/intern/country/us/state/az/', 'AZ'),
            'microchip':Microchip('microchip', 'https://careers.microchip.com/jobsearch/#All~Job~Categories|US+AZ+Tempe;US+AZ+Chandler||d-ASC|1', 'AZ')
            }
    
    def scrape_jobs(self):
        '''
        This function is used to scrape all the jobs off the web
        '''
        #get all jobs
        for company in self.company_dict.values():
            company.scrape_jobs()

    def get_jobs(self):
        '''
        This function is used to get the jobs from company list. If companies is None, get all the jobs, otherwise onlie get jobs from companies
        '''
        pass
