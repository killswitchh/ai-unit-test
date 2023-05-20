from enum import Enum
 
class Parser(str, Enum):
    REDBARON = 'REDBARON'


class OpenAiRoles(str, Enum):
    SYSTEM = 'system'    
    USER = 'user'
    ASSISTANT = 'assistant'

class OpenAiModels(str, Enum):
    def to_json(self):
        return self.message
    TURBO_3_5 = 'gpt-3.5-turbo'    
    