import cv2
from PIL import Image
from pytesseract import pytesseract
cap=cv2.VideoCapture(0)
while True:
    _,img=cap.read()
    cv2.imshow("Text Detection",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):   
        cv2.imwrite('test1.jpg',img)
        break
cap.release()
cv2.destroyAllWindows()
def tesseract():
    path="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    imgpath="D:\\python\\04d3b97b08093b9be3b2514c9fb0dbe7.jpg"    
    pytesseract.tesseract_cmd=path
    text=pytesseract.image_to_string(Image.open(imgpath))
    data=text.split(" ")
    amount=[]
    print(data)
    for i in data:
        if i.find('$')==-1:
            continue
        else:
            cost=""
            for j in i:
                if j!='\n':
                    cost=cost+j
                    
                else:
                    amount.append(cost)
                    break
            
            
    print(amount)        
tesseract()
    