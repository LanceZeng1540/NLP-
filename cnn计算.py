#encoding:utf8
import numpy as np

def cnn(input_img, kernelsize=3, padding=0,stride = 2,cout=4):
    
    inchannel, img_h, img_w = input_img.shape
    output_h = int((img_h-kernelsize+2*padding)/stride+1)
    output_w = int((img_w-kernelsize+2*padding)/stride+1)
    output_img = np.ones((cout, output_h, output_w))
    
    #padding处理
    input_img = np.pad(input_img, ((0,0),(padding,padding),(padding,padding)), 'constant')
    
    #输出多通道 多个卷积核
    for oc_index in range(cout):
        kernel = np.random.random((inchannel, kernelsize, kernelsize))
        output_img_sc = output_img[oc_index, ...]
        #多通道 1个卷积核
        for h in range(output_h):
            for w in range(output_w):
                field_h = h*stride
                field_w = w*stride
                #获取原图的单个通道
                result = 0
                #单个通道 1个卷积核
                for ic_index in range(inchannel):
                    input_img_sc = input_img[ic_index,...]
                    kernel_sc = kernel[ic_index,...]
                    #获取感受野
                    field = input_img_sc[field_h:field_h+kernelsize,field_w:field_w+kernelsize]
                    result += np.sum(np.multiply(field,kernel_sc))
                output_img_sc[h,w] = result
    return output_img
    
if __name__=='__main__':
    #输入图片
    img_2d = np.arange(75).reshape(15, 5)
    img_3d = np.arange(75).reshape(3, 5, 5)
    
    output_img = cnn(img_3d, kernelsize=3, padding=1, stride=2, cout=4)
    print(output_img.shape)
    #np.pad(array, padwidth, mode)函数
    #padwidth:数值或者元祖，如果是元祖：((1,1),(1,1),(1,1))
    #print(img_3d)
    #print(np.pad(img_3d, ((0,0),(1,1),(1,1)), 'constant'))
    