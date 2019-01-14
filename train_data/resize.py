from PIL import Image
import os.path
import glob


def convertjpg(jpgfile,outdir,width=600,height=800):
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)   
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
for jpgfile in glob.glob("train_data\\pic2\\*.jpg"): # 绝对路径
    convertjpg(jpgfile,"train_data\\pic3")
