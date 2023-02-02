import qrcode
import qrcode.image.pil

##version qrcode =7.4

#def genarate_qrcode(url, file_name):

image_qr = qrcode.make("http://localhost:8501")
type(image_qr)

image_qr.save("img_ia.png")



##genarate_qrcode("http://localhost:8501", "qr_image.png")


#img = qrcode_test.make('some date here')
#type(img)

#img.save("some_file.png")