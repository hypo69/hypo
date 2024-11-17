

"""! HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! """

import header
from src import gs
from src.utils.file import read_text_file, save_text_file, recursively_get_filepath
from src.utils.printer import pprint

images_path = recursively_get_filepath(gs.path.google_drive / 'kazarinov' / 'converted_images' / 'pastel', ['*.jpeg','*.jpg','*.png'])
pprint(images_path)
...