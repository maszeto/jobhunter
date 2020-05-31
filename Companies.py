from Job import Job
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

    
    def print_jobs(self):
        for job in self.job_list:
            print("Title: {}".format(job.title))
            print("Date: {}".format(job.date))
            print("Link: {}".format(job.link))
            print("ID: {}\n".format(job.job_id))

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
            title = job_elem.find('a').text.split(' - ')[1]
            date =''
            job_id = job_elem.find('a').text.split(' - ')[0]
            link = job_elem.find('a', href=True)['href']
            self.job_list.append(Job(title, link, date, job_id))
        
        self.print_jobs()
        