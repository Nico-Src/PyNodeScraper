from src.resource_manager import ResourceManager;
from src.scraper import Scraper;

global resourceManager, scraper;
resourceManager = ResourceManager();
scraper = Scraper();

def getResourceManager():
    return resourceManager;

def getScraper():
    return scraper;