from django.core.management.base import BaseCommand
from characterManager.models import CharacterClass, Server


#List od servers
SERVER_LIST = [
    'tylezia','tal kasha', 'orukam', 
    'Imagiro', 'Hell Mina', 'Draconiros', 
    'Ombre'
]

# List of personnage
PERSONNAGE_CLASS_LIST = [
    'ecaflip', 'cra',
    'eniripsa', 'iop', 'feca',
    'sacrieur', 'sadida', 'osamodas',
    'enutrof', 'sram', 'xelor',
    'pandawa', 'roublard', 'zobal', 'steamer',
    'eliotrope', 'huppermage', 'ourignak', 'forgelance'
]


class Command(BaseCommand):
    help = 'Import dofus information handle manually'
    
    def handle(self, *args, **kwargs):

        # TODO: See how to delete the data before
        # Clean database
        # Server().objects.all().delete()
        # CharacterClass().objects.all().delete() 


        for _server in SERVER_LIST:
            server = Server(name=_server)
            server.save()

        for _characterClass in PERSONNAGE_CLASS_LIST:
            perso = CharacterClass(name= _characterClass, 
                                   logo_url= f'/static/image/logo_personnage/{_characterClass}.png')
            perso.save()
