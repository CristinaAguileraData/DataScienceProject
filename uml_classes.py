#SUPERCLASS
class IdentifiableEntity(object):
    def __init__(self, id):
        self.id= id

    def getId(self):
        return self.id


#CLASS_2
class Person(IdentifiableEntity):
    def __init__(self, id:str, name:str):
        self.name= name # its attribute
        super().__init__(id) #inherited attribute  

    def getName(self):
        return self.name

#CSV

#CLASS_1
class CulturalHeritageObject(IdentifiableEntity):
    def __init__(self, id:str, title:str, owner:str, place:str, hasAuthor:list[Person], date:str|None):# now has its own parameters + inherited + relationship has author
        self.title= title #title is mandatory
        self.date= date  #optional so possibly None as default
        self.owner= owner
        self.place= place
        super().__init__(id) #explicitly states that chobj inherits id from superclass
        self.hasAuthor= hasAuthor

    def getTitle(self):
        return self.title

    def getDate(self):
        return self.date

    def getOwner(self):
        return self.owner

    def getPlace(self):
        return self.place

    def getAuthors(self):
        return self.hasAuthor

        
    
#SUBCLASSES OF CLASS_1 (subclasses of culturalHeritageObject)
class NauticalChart(CulturalHeritageObject):
    pass

class ManuscriptPlate(CulturalHeritageObject):
    pass

class ManuscriptVolume(CulturalHeritageObject):
    pass

class PrintedVolume(CulturalHeritageObject):
    pass

class PrintedMaterial(CulturalHeritageObject):
    pass

class Herbarium(CulturalHeritageObject):
    pass

class Specimen(CulturalHeritageObject):
    pass

class Painting(CulturalHeritageObject):
    pass

class Model(CulturalHeritageObject):
    pass

class Map(CulturalHeritageObject):
    pass

#JSON

#CLASS_3
class Activity(object):
    def __init__(self, institute:str, refersTo:CulturalHeritageObject, person:str|None, tool:set[str], start:str|None, end:str|None): #now has its attribute + relationship to chobj refersTo
        self.institute=institute
        self.person=person
        self.tool= tool 
        self.start=start
        self.end=end
        self.refersTo= refersTo

    def getResponsibleInstitute(self):
        return self.institute

    def getResponsiblePerson(self):
        return self.person

    def getTools(self):
        return self.tool

    def getStartDate(self):
        return self.start

    def getEndDate(self):
        return self.end

    def referTo(self):
        return self.refersTo  #check for recursivity: same name variable and method may have to change name of the variable




#SUBCLASSES of class_3 (subclasses of Activity)
class Acquisition(Activity):
    def __init__(self, institute:str, person:str|None, tool:set[str], start:str|None, end:str|None, refersTo:CulturalHeritageObject, technique:str): #has now its attributes and these inherited
        self.technique= technique
        super().__init__(institute, person, tool, start, end, refersTo,)

    def getTechnique(self):
        return self.technique


class Processing(Activity):
    pass
class Modelling(Activity):
    pass
class Optimising(Activity):
    pass
class Exporting(Activity):
    pass