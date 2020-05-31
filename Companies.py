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

class Microchip(Company):
    def scrape_jobs(self):

        #This is the base URL, however there are multiple pages, append the page number to the end of the url 
        #for example 
        #https://careers.microchip.com/jobsearch/#All~Job~Categories|US+AZ+Tempe;US+AZ+Chandler||d-ASC|1
        #is page 1
        #We can start page 1 and scrape the number of job listings to figure out the number of pages, since 10 jobs are shown per page.
        #Sike, the total number of jobs is generated by js so we can't see it D:, so just sent requests till we don't get a response
        #Double sike, idk why but if you type in 100 it still takes you to a page, just one with no job listings, so lets go until we don't find any jobs
        #doubt there will ever be more than 20 pages, so let's set that as our max

        for page in range(20):
            
            URL = 'https://careers.microchip.com/jobsearch/#All~Job~Categories|US+AZ+Tempe;US+AZ+Chandler||d-ASC|' + str(page + 1)
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            job_list = soup.find_all(id = 'job-list-items')
            for job in job_list:
                print(job.find('div', 'jobTitle underlineMe'))
