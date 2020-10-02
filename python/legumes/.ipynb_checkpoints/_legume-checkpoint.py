from dataclasses import dataclass as _dataclass
from typing import List as _List


__all__=["Legume"]

class Legume:
    '''A legume in the tool'''
    name: str = None
    legume_type: str = None    
    
        
    food: int = None
    feed: int = None
    income: int = None
    erosion_control: int = None
    fuel: int = None
    soil_fertility: int= None
    
    land_required: int = None
    labour_required: int = None
    seed_supply_required: int = None
    inputs_and_services_required: int = None
    knowledge_and_skills_required: int = None
    water_required: int = None
    markets_required: int = None
        
        
        
    def is_null(self) -> bool:
        return self.name is None
        
    def assert_sane(self):

        if self.name is None:
            self = Legume()
            return
        
        
        
        assert self.name is not None, "Need a value for name"
        self.land_required = str(self.name)
        
        assert self.legume_type is not None, "Need a value for legume_type"
        self.legume_type = str(self.legume_type)
        
        assert self.land_required is not None, "Need a value for land_required"
        self.land_required = int(self.land_required)
        assert self.land_required >=0, "land_required score must be between 0 and 4"
        assert self.land_required <=4, "land_required score must be between 0 and 4"

        assert self.labour_required is not None, "Need a value for labour_required"
        self.labour_required = int(self.labour_required)
        assert self.labour_required >=0, "labour_required score must be between 0 and 4"
        assert self.labour_required <=4, "labour_required score must be between 0 and 4"

        assert self.seed_supply_required is not None, "Need a value for seed_supply_required"
        self.seed_supply_required = int(self.seed_supply_required)
        assert self.seed_supply_required >=0, "seed_supply_required score must be between 0 and 4"
        assert self.seed_supply_required <=4, "seed_supply_required score must be between 0 and 4"

        assert self.inputs_and_services_required is not None, "Need a value for inputs_and_services_required"
        self.inputs_and_services_required = int(self.inputs_and_services_required)
        assert self.inputs_and_services_required >=0, "inputs_and_services_required score must be between 0 and 4"
        assert self.inputs_and_services_required <=4, "inputs_and_services_required score must be between 0 and 4"

        assert self.knowledge_and_skills_required is not None, "Need a value for knowledge_and_skills_required"
        self.knowledge_and_skills_required = int(self.knowledge_and_skills_required)
        assert self.knowledge_and_skills_required >=0, "knowledge_and_skills_required score must be between 0 and 4"
        assert self.knowledge_and_skills_required <=4, "knowledge_and_skills_required score must be between 0 and 4"

        assert self.water_required is not None, "Need a value for water_required"
        self.water_required = int(self.water_required)
        assert self.water_required >=0, "water_required score must be between 0 and 4"
        assert self.water_required <=4, "water_required score must be between 0 and 4"

        assert self.markets_required is not None, "Need a value for markets_required"
        self.markets_required = int(self.markets_required)
        assert self.markets_required >=0, "markets_required score must be between 0 and 4"
        assert self.markets_required <=4, "markets_required score must be between 0 and 4"


        assert self.food is not None, "Need a value for food"
        self.food = int(self.food)
        assert self.food >=0, "food score must be between 0 and 4"
        assert self.food <=4, "food must be between 0 and 4"

        assert self.feed is not None, "Need a value for feed"
        self.feed = int(self.feed)
        assert self.feed >=0, "feed score must be between 0 and 4"
        assert self.feed <=4, "feed score must be between 0 and 4"

        assert self.income is not None, "Need a value for income"
        self.income = int(self.income)
        assert self.income >=0, "income score must be between 0 and 4"
        assert self.income <=4, "income score must be between 0 and 4"

        assert self.erosion_control is not None, "Need a value for erosion_control"
        self.erosion_control = int(self.erosion_control)
        assert self.erosion_control >=0, "erosion_control score must be between 0 and 4"
        assert self.erosion_control <=4, "erosion_control score must be between 0 and 4"

        assert self.fuel is not None, "Need a value for fuel"
        self.fuel = int(self.fuel)
        assert self.fuel >=0, "fuel score must be between 0 and 4"
        assert self.fuel <=4, "fuel score must be between 0 and 4"

        assert self.soil_fertility is not None, "Need a value for soil_fertility"
        self.soil_fertility = int(self.soil_fertility)
        assert self.soil_fertility >=0, "soil_fertility score must be between 0 and 4"
        assert self.soil_fertility <=4, "soil_fertility score must be between 0 and 4"

    def toDry(self):
        
            self.assert_sane()

            if self.is_null():
                return {}

            return {"name": self.name,
                    "legume_type": self.legume_type,
                    "food": self.food,
                    "feed": self.feed,
                    "income": self.income,
                    "erosion_control": self.erosion_control,
                    "fuel": self.fuel,
                    "soil_fertility": self.soil_fertility,
                    "land_required": self.land_required,
                    "labour_required": self.labour_required,
                    "seed_supply_required": self.seed_supply_required,
                    "inputs_and_services_required": self.inputs_and_services_required,
                    "knowledge_and_skills_required": self.knwoledge_and_skills_required,
                    "water_required": self.water_required,
                    "markets_required": self.markets_required
            }

