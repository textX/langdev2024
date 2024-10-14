from os.path import dirname, join

from textx import generator, language, metamodel_from_file
from textxjinja import textx_jinja_generator


@language("Drone", ".dr")
def drone():
    "A language for giving flight commands to drone"
    return metamodel_from_file(join(dirname(__file__), "drone.tx"))


@generator('Drone', 'python')
def drone_generator(metamodel, model, output_path, overwrite, debug):
    "Generate executable python script from Drone model"
    
    current_dir = dirname(__file__)
    templates_path = join(current_dir, 'template')
    default_output_path = join(current_dir, '..', 'dist')

    context = {
        'commands': model.commands
    }

    textx_jinja_generator(templates_path, output_path or default_output_path, context, overwrite)