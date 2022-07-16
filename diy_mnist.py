from PIL import Image
import os

#a4图片储存路径
path = 'a4imgs'

# 建立文件夹
if os.path.exists('data_set'):
    print("数据集储存文件夹已存在")
else:
    os.mkdir('data_set')
    print("数据集储存文件夹已建立")
for i in range(10):
    if os.path.exists('data_set/'+str(i)):
        pass
    else:
        os.mkdir('data_set/'+str(i))
        
# 获取图片列表
def get_imgs(path):  # 获取所有文件
    imgs_list = []
    for i,name in enumerate(os.listdir(path)): #listdir返回文件中所有目录
        os.rename(path + '/' + name,path + '/' +'{}.png'.format(i)) # 重命名图片
        imgs_list.append('{}.png'.format(i))
    return imgs_list
  
# 切割图片
def cut_image(imgs_list):
    for i in range(4):        #遍历切割区域
        for j in range(len(imgs_list)):   #遍历a4图片
            img = Image.open('a4imgs/'+imgs_list[j])
            
            # 获取图像的宽高
            img_size = img.size
            w = img_size[0] 
            h = img_size[1]
            #计算剪裁长度
            x_step = w*0.25
            y_step = h*0.25
            z = (x_step-y_step)/2
            
            # 切割折痕区域-->转化为正方形-->调整像素-->调整rgb-->保存图片
            img.crop((i*x_step,0,(i+1)*x_step,y_step)).crop((z,0,y_step+z,y_step)).resize((28, 28)).convert('L').save('data_set/{}/{}_{}.png'.format(i,j,i))
            img.crop((i*x_step,y_step,(i+1)*x_step,y_step*2)).crop((z,0,y_step+z,y_step)).resize((28, 28)).convert('L').save('data_set/{}/{}_{}.png'.format(i+4,j,i+4))
            if i <= 1:
                img.crop((i*x_step,y_step*2,(i+1)*x_step,y_step*3)).crop((z,0,y_step+z,y_step)).resize((28, 28)).convert('L').save('data_set/{}/{}_{}.png'.format(i+8,j,i+8))
            else:
                pass
              
imgs_list = get_imgs(path)
cut_image(imgs_list)
