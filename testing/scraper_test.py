from bs4 import BeautifulSoup
from lib.Scraper import Scraper

class Test_Scraper:
    '''Scraper in Scraper.py'''

    def test_get_page(self):
        "uses Beautiful Soup to get the HTML from a web page"
        scraper = Scraper()
        doc = scraper.get_page()
        assert(isinstance(doc, BeautifulSoup))

    def test_get_courses(self):
        "Test get_courses"
        scraper = Scraper()
        course_offerings = scraper.get_courses()
        assert(len(course_offerings) != 0)
        for course in course_offerings:
            assert(isinstance(course, element.tag))

    def test_make_courses(self):
        "Test self.courses"
        #isinstance(var, str)
        scraper = Scraper()

        courses = scraper.make_courses()
        
        assert(isinstance(courses, list))
        assert(len(courses) != 0)

        for course in courses:
            assert(isinstance(course.title, str))
            assert(isinstance(course.schedule, str))
            assert(isinstance(course.description, str))
