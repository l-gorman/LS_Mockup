from dataclasses import dataclass as _dataclass


__all__ = ["LegumeType"]

@_dataclass
class LegumeType:
    legume_type: str = None
    legume_type_code: str = None
    def is_null(self):
        return self.legume_type is None
    
    def assert_sane(self):
        if self.legume_type is None:
            self = LegumeType()
            return 
        assert self.legume_type is not None, "Need to include string argument legume_type"
        self.legume_type=str(self.legume_type)
        
        assert self.legume_type_code is not None, "Need to include string argument legume_type_code"
        self.legume_type_code=str(self.legume_type_code)
        
        assert len(self.legume_type_code) == 2, "legume_type_code is meant to be length 2"
        
        assert self.legume_type_code.isalpha(), "legume_type_code is meant to be letters only"
        self.legume_type_code=self.legume_type_code.upper()

    
        
    def toDry(self):
        self.assert_sane()
        
        if self.is_null():
            return {}
        return {"legume_type_code": self.legume_type_code,
                "legume_type": self.legume_type}
        
        