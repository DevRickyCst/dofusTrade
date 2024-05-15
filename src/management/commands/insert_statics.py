from django.core.management.base import BaseCommand
from characterManager.models import CharacterClass, Server


SERVER_LIST = [
    'tylezia','tal kasha', 'orukam', 
    'Imagiro', 'Hell Mina', 'Draconiros', 
    'Ombre'
]

PERSONNAGE_CLASS_LIST = [
    'ecaflip', 'cra',
    'eniripsa', 'iop', 'feca',
    'sacrieur', 'sadida', 'osamodas',
    'enutrof', 'sram', 'xelor',
    'pandawa', 'roublard', 'zobal', 'steamer',
    'eliotrope', 'huppermage', 'ourignak'
]



class Command(BaseCommand):
    help = 'Import dofus information handle manually'
    
    def handle(self, *args, **kwargs):


        for _server in SERVER_LIST:
            server = Server(name=_server)
            server.save()

        for personnage in PERSONNAGE_CLASS_LIST:
            perso = CharacterClass(name= personnage, logo_url= f'static/image/logo_personnage/{personnage}.png')
            perso.save()
