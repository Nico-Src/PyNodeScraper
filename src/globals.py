from src.resource_manager import ResourceManager;
from src.scraper import Scraper;

global resource_manager, scraper;
resource_manager = ResourceManager();
scraper = Scraper();

def get_resource_manager():
    return resource_manager;

def get_scraper():
    return scraper;