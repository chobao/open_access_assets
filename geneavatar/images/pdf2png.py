# import module
from pdf2image import convert_from_path
 
name = 'framework'
# Store Pdf with convert_from_path function
images = convert_from_path(f'./{name}.pdf', dpi=500)
 
images[0].save(f'{name}.png', 'PNG')