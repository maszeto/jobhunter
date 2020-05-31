import Job
from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup

class Company(ABC):
    '''
    The company class holds all related jobs and company info
    '''
    def __init__(self, name, jobsite, location):
        
        self.name = name
        self.jobsite = jobsite
        self.loc = location
        self.job_list = []
    @abstractmethod
    def scrape_jobs(self):
        '''
        This function webscrapes all the jobs using python, it's call depends on which company, so it is abstract
        '''
        pass
        
class Intel(Company):
    
    def scrape_jobs(self):
        print("CALLED")
        URL = 'https://jobs.intel.com/ListJobs/All/Search/jobtitle/intern/country/us/state/az/'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        job_elems = soup.find_all('td', class_='coljobtitle')
        for job_elem in job_elems:
            print(job_elem.find_all(href=True))
