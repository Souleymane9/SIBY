import re 
from pydantic import BaseModel, validator
from typing import List
from ModelMusique import ModelMusique


class ModelMagasin(BaseModel):
    type_music: str
    music_vinyle: List[ModelMusique]
    music_DVD: List[ModelMusique]
    
    


def ajouter_vinyle(self, musique: ModelMusique):
    self.vinyles.append(musique)
     

def retirer_vinyle(self,musique: ModelMusique):
    self.music_vinyle.remove(musique)
    
    
def ajouter_DVD(self, musique: ModelMusique):
    self.music_DVD.append(musique)
    
     
def remove_DVD(self, musique: ModelMusique):
    self.music_DVD.REMOVE(musique)
    
## Verification si type musique n'est pas égal à style de musique
def verif(self, musique: ModelMusique):
    style= musique.immatriculation[7:9]
    if style != self.type_music:
        return False 
    else:
        return True

    
    