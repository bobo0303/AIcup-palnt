import csv, os, docx

#doc = docx.Document('C:/Users/wiwiw/OneDrive/桌面/plan/2022.docx')
path = 'C:/Users/wiwiw/OneDrive/桌面/plan'
list = ['banana', 'bareland', 'carrot', 'corn', 'dragonfruit', 'garlic', 'guava', 'bareland', 'peanut', 'pineapple', 'pumpkin', 'rice', 'soybean', 'sugarcane', 'tomato']
#list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

#if not os.path.isdir(path+'/20_efficientnet_b5.csv'):
#    os.makedirs(path+'/20_efficientnet_b5.csv')

file = open(path+'./10_b5.csv',mode='w', newline='')
writer = csv.writer(file)
#writer.writerow(['image_filename', 'label'])
writer.writerow(['banana', 'bareland', 'carrot', 'corn', 'dragonfruit', 'garlic', 'guava', 'bareland', 'peanut', 'pineapple', 'pumpkin', 'rice', 'soybean', 'sugarcane', 'tomato'])


file = path + './10_b5.log'

'''

for line in open ( file , "r" ,encoding= 'UTF-8' ):
    #print(line)
    a = str(line[84:100])
    b = a.split(',')
    #print(b[1])
    #print(list[int(b[1])])
    c = [str(line[68:84]), list[int(b[1])]]
    print(c)
    writer.writerow([str(line[68:84]), list[int(b[1])]])
'''

for line in open ( file , "r" ,encoding= 'UTF-8' ):
    # print(line)
    #a = str(line[84:100])
    b = line.split(',')
    print(b)
    print(line[0:4] + ' ' + line[5:9] + ' ' + line[10:14] + ' ' + line[15:19] + ' ' + line[20:24] + ' ' + line[25:29] + ' ' + line[30:34] + ' ' + line[35:39] + ' ' + line[40:44] + ' ' + line[45:49] + ' ' + line[50:54] + ' ' + line[55:59]
          + ' ' + line[60:64] + ' ' + line[65:69] + ' ' + line[70:74] + ' ' + line[75:79] + ' ' + line[80:84] + ' ' + line[85:89] + ' ' + line[90:94] + ' ' + line[95:99])
    #c = [str(line[68:84]), list[int(b[1])]]
    #print(c)
    writer.writerow([line[0:4], line[5:9], line[10:14], line[15:19], line[20:24], line[25:29], line[30:34], line[35:39], line[40:44], line[45:49], line[50:54],  line[55:59], line[60:64], line[65:69], line[70:74], line[75:79], line[80:84] , line[85:89],  line[90:94], line[95:99]])
