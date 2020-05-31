from Companies import Intel


class Manager:
    '''
    This class manages all the job listings by company
    '''

    def __init__(self):
        self.company_dict = {
            'intel':Intel('intel', 'https://jobs.intel.com/ListJobs/All/Search/jobtitle/intern/country/us/state/az/', 'AZ')
            }
    
    def scrape_jobs(self, companies = None):
        '''
        This function is used to get the jobs from company list. If companies is None, get all the jobs, otherwise onlie get jobs from companies
        '''
        if(companies == None):
            print("CALLED")
            #get all jobs
            for company in self.company_dict.values():
                company.scrape_jobs()
        else:
            #get only specified jobs
            pass