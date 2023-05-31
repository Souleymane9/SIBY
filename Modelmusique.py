import re 
from pydantic import BaseModel, validator


class ModelMusique(BaseModel):
    titre_musique:str
    non_musique: str
    immat_musique: str
    
    
@validator("immat_musique")
def immat_verif(cls, value): 
    value = 15
    
    if len(value)!=15:
     raise ValueError("Immatriculation invalide")
     return value 
 
@validator("immat_2_lettres")
def two_char_verif(cls, value):
    resultat= isinstance(value,str)
    if resultat != 1:
        raise ValueError("2 premiers caractéres invalides")
    return value

@validator("immat_3_")
def three_digit_verif(cls, value):
    nbr= value[3:5]
        
    if not nbr.isdigit() or nbr<60 or nbr>300:
        raise ValueError("Immatriculation invalide")
    return value
    
@validator("Immat")
def type_Rap(cls, value):
    List_rap= ["POP","RAP","RNB"]
    position= value[7:9]
    
    if position not in  List_rap:
        raise ValueError("Immatriculation invalide")
    return value 
        


@validator("Immat")
def verif_Slash(cls, value):
    Sash_1= value[2]
    Sash_2= value[6]
    Sash_3= value[10]
    if Sash_1 != '/' or Sash_2 != '/' or Sash_3 != '/':
      raise ValueError("Immmatriculation invalide")   
    
@validator("Immat")
def type_Rap(cls, value):
    premier1= value[11]
    premier2= value[12]
    premier3= value[13]
    premier4= value[14]
    if (premier1 =='6' or premier2=='6'or  premier3=='6' or  premier3=='6' or  premier4=='6'):
        raise ValueError("Immatriculation invalide")
    return value