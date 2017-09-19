from pptx import Presentation
from pptx.util import Inches
import csv

studentdata = csv.reader(open('PWAverage.csv'))
prs = Presentation('test.pptx')
blank_slide_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank_slide_layout)

r = 0
placeholder = 0
left = 0.5
top = 0.5
width = 1
height = 1

for row in studentdata:
	if r > 0:
		if placeholder == 42:
			slide = prs.slides.add_slide(blank_slide_layout)
			placeholder = 0
			left = 0.5
			top = 0.5
		if placeholder == 14 or placeholder == 28:
			left = left + 3
			top = 0.5
		
		first_name = row[1]
		last_name = row[2]
		pwa = row[4]
		textBox = slide.shapes.add_textbox(Inches(left),Inches(top),Inches(width),Inches(height))
		textBox.text_frame.text = first_name  + last_name + " - " + pwa
		placeholder = placeholder+1
		top = top+0.5
	r = r+1

prs.save('studentTest.pptx')