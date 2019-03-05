"""
An example how to generate angularjs code from textX model using jinja2
template engine (http://jinja.pocoo.org/docs/dev/)
"""
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm


def main(debug=False):

    this_folder = dirname(__file__)

    entity_mm = get_entity_mm(debug)

    #Construye un modelo de tarea desde el archivo tarea.ent 
    tarea_model = entity_mm.model_from_file(join(this_folder, 'tarea.ent'))

    def is_entity(n):
        #Comprueba si es una entidad
        if n.type in tarea_model.entities:
            return True
        else:
            return False

    def javascript_type(s):
        """
        Maps type names from PrimitiveType to Java.
        """
        return {
                'variable': 'var'
        }.get(s.name, s.name)


    # Create output folder
    srcgen_folder = join(this_folder, 'srcgen')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Register filter for mapping Entity type names to Java type names.

    jinja_env.tests['entity'] = is_entity

    jinja_env.filters['javascript_type'] = javascript_type   

    # Load template
    template = jinja_env.get_template('estilos.template')

   

    

    for entity in tarea_model.entities:
        # For each entity generate java file
        with open(join(srcgen_folder,
                       "estilos%s.css" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

    # Load template
    template = jinja_env.get_template('main.template')
    for entity in tarea_model.entities:
        # For each entity generate java file
        with open(join(srcgen_folder,
                       "%smain.js" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))        


     # Load template
    template = jinja_env.get_template('tarea.template')
    for entity in tarea_model.entities: 
        # For each entity generate java file
        with open(join(srcgen_folder,
                       "index.html"), 'w') as f:
            f.write(template.render(entity=entity,
                                     names    = ["Dormir", "Estudiar", "ver Tele"],))        

    
if __name__ == "__main__":
    main()
