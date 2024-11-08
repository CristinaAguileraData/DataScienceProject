from pandas import DataFrame, Series, read_json
from uml_classes import IdentifiableEntity, CulturalHeritageObject, Person


class Handler(object):
    def __init__(self, dbPathOrUrl):
        self.dbPathOrUrl = dbPathOrUrl
        self.data_path = set()  # creazione del set 


    def getDbPathOrUrl(self): # definizione metodo getDbPathOrUrl
        return self.dbPathOrUrl  
    
    def setDbPathOrUrl(self, pathOrUrl): # definizione metodo setDbPathOrUrl
        result = True
        if pathOrUrl not in self.data_path:  
            self.data_path.add(pathOrUrl)
        else:
            result = False
        return result


class UploadHandler(Handler): 
    def __init__(self, dbPathOrUrl):
        super().__init__(dbPathOrUrl)
        
    def pushDataToDb(self, path): # definizione metodo pushDataToDb
        self.data_paths = set()
        result = True
        if path not in self.data_paths:  
            self.data_paths.add(path)
        else:
            result = False
        return result

# DB CREATION

class MetadataUploadHandler(UploadHandler):
    def __init__(self, dbPathOrUrl):
        super().__init__(dbPathOrUrl)
    

class ProcessDataUploadHandler(UploadHandler):
    pass


class QueryHandler(Handler):
    def __init__(self, dbPathOrUrl):
        super().__init__(dbPathOrUrl)
        
    def getById(self, id):
        self.id = id
        data_frame = read_json(self.dbPathOrUrl)
        return DataFrame({
            "id": id,
            "title": CulturalHeritageObject.getTitle(),
            "name": Person.getName()
        })


class MetadataQueryHandler(QueryHandler):
    def __init__(self, dbPathOrUrl):
        super().__init__(dbPathOrUrl)
        # prova: forse prima di costruire il DataFrame bisogna richiamare il database ?
        data_frame = read_json(self.dbPathOrUrl)
        
    def getAllPeople(self):
        # prova
        # data_frame_people = data_frame["Author"]
        return DataFrame({
            "id": Person.getId(),
            "person": Person.getName()
        })
    
    def getAllCulturalHeritageObjects(self):
        return DataFrame({
            "id": CulturalHeritageObject.getId(),
            "title": CulturalHeritageObject.getTitle()
        })
    
    def getAuthorsOfCulturalHeritageObject(self, objectId):
        self.objectId = objectId
        return DataFrame({
            "id": CulturalHeritageObject.getId(),
            "author": CulturalHeritageObject.getAuthors()
        })