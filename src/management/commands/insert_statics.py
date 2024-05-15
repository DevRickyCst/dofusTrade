from django.core.management.base import BaseCommand
from characterManager.models import 


SERVER_LIST = {
    'tylezia','tal kasha', 'orukam', 'Imagiro', 'Hell Mina', 'Draconiros', 'Ombre'
}


class Command(BaseCommand):
    help = 'Description of what your command does'

    def add_arguments(self, parser):
        # Define any arguments here
        #parser.add_argument('arg1', type=str, help='Argument 1 description')
        return 0
    

    def handle(self, *args, **kwargs):
        # Extract the arguments
        #arg1 = kwargs['arg1']
        #option1 = kwargs.get('option1')

        # Your custom script logic here
        self.stdout.write(f'Argument 1: {arg1}')
        if option1:
            self.stdout.write(f'Optional argument: {option1}')
        self.stdout.write('Custom command executed successfully!')