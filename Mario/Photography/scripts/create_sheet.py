import os
import tempfile
from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage
from PIL import Image as PILImage

downsized_dir = '../downsized'
excel_path = './photos_list.xlsx'
temp_files = []

wb = Workbook()
ws = wb.active
ws.append(['#', 'Photo', 'Name', 'Description'])
ws.column_dimensions['B'].width = 85.7

for filename in os.listdir(downsized_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
        img_path = os.path.join(downsized_dir, filename)
        photo_name = os.path.splitext(filename)[0]
        ws.append([photo_name, '', '', ''])
        row_num = ws.max_row

        with PILImage.open(img_path) as im:
            im.thumbnail((600, 600))
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
                im.save(tmp.name)
                temp_files.append(tmp.name)

        img = XLImage(temp_files[-1])
        img.anchor = f'B{row_num}'
        ws.add_image(img)
        ws.row_dimensions[row_num].height = 600 * 0.75

wb.save(excel_path)

for temp_path in temp_files:
    os.remove(temp_path)