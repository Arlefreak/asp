from modeltranslation.translator import translator, TranslationOptions
from models import *

class ProyectTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

class singleInformationTranslationOptions(TranslationOptions):
    fields = ('aboutText',)

class PressTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

#translator.register(Proyect, ProyectTranslationOptions)
#translator.register(singleInformation, singleInformationTranslationOptions)
#translator.register(Press, PressTranslationOptions)