import io
import easyocr
import urllib.request

class Extraction :
    def __init__(self):
        self.reader=easyocr.Reader(['en'])
        
    def readText(self,path):
        print("read")
        result=self.reader.readtext(path,detail=0)
        print(result)
        return result
