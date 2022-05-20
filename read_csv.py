import csv, os, docx
from collections import Counter
import random

path = 'C:/Users/wiwiw/OneDrive/桌面/plan'
list = ['banana', 'bareland', 'carrot', 'corn', 'dragonfruit', 'garlic', 'guava', 'bareland', 'peanut', 'pineapple', 'pumpkin', 'rice', 'soybean', 'sugarcane', 'tomato']


#if not os.path.isdir(path+'/20_efficientnet_b5.csv'):
#    os.makedirs(path+'/20_efficientnet_b5.csv')

file = open(path+'./last_csv.csv',mode='w', newline='')
writer = csv.writer(file)
writer.writerow(['image_filename', 'label'])

with open('C:/Users/wiwiw/OneDrive/桌面/plan/10_b4.csv', newline='') as csvfile11:
    rows11 = csv.reader(csvfile11)

    with open('C:/Users/wiwiw/OneDrive/桌面/plan/10+10_b4.csv', newline='') as csvfile22:
        rows22= csv.reader(csvfile22)

        with open('C:/Users/wiwiw/OneDrive/桌面/plan/10_b5.csv', newline='') as csvfile33:
            rows33 = csv.reader(csvfile33)

            with open('C:/Users/wiwiw/OneDrive/桌面/plan/10_efficientnet_b4/10_efficientnet_b4.csv', newline='') as csvfile1:
                rows1 = csv.reader(csvfile1)

                with open('C:/Users/wiwiw/OneDrive/桌面/plan/b4_10+10_97/10+10_efficientnet_b4.csv', newline='') as csvfile2:
                    rows2= csv.reader(csvfile2)

                    with open('C:/Users/wiwiw/OneDrive/桌面/plan/model_b5_20_dataupup/20_efficientnet_b5.csv', newline='') as csvfile3:
                        rows3 = csv.reader(csvfile3)

                        row11 = [roww11 for roww11 in rows11]
                        row22 = [roww22 for roww22 in rows22]
                        row33 = [roww33 for roww33 in rows33]
                        row1 = [roww1 for roww1 in rows1]
                        row2 = [roww2 for roww2 in rows2]
                        row3 = [roww3 for roww3 in rows3]
                        line = len(row1)
                        n1=n2=n3=n33=n333=p1=p2=0

                        for n in range(line):
                            if row1[n][1] == 'label':
                                continue
                            #print(row1[n][1] +' '+ row2[n][1] +' '+ row3[n][1], row1[n][0])
                            #max(row1[n][1],row2[n][1],row3[n][1])

                            '''if row1[n] == row2[n]  and row3[n] == row2[n] and row1[n] == row3[n]:
                                print(row1[n][0] +' '+ row1[n][1] +' '+ row2[n][1] +' '+ row3[n][1])
                                writer.writerow([row1[n][0], row1[n][1]])
                                n1+=1'''
                            if row1[n] == row2[n] and row3[n] == row2[n] and row1[n] == row3[n]:
                                a = list.index(row1[n][1])
                                b = list.index(row2[n][1])
                                c = list.index(row3[n][1])
                                aa = row11[n][a]
                                bb = row22[n][b]
                                cc = row33[n][c]
                                listt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                                listt.pop(a)
                                list_r = [a]
                                # print(len(listt))
                                count = 0

                                for xx in range(len(listt)):
                                    axx = float(aa) - float(row11[n][listt[xx]])
                                    # print(axx)
                                    bxx = float(bb) - float(row22[n][listt[xx]])
                                    # print(bxx)
                                    cxx = float(cc) - float(row33[n][listt[xx]])
                                    # print(cxx)
                                    if 0 <= axx == 0 and bxx == 0 and cxx == 0:
                                        # print(axx, bxx, cxx, row1[n][0], row3[n][1])
                                        count += 1
                                        list_r.append(listt[xx])
                                if count == 0:
                                    writer.writerow([row1[n][0], row1[n][1]])
                                elif count != 0:
                                    # print(list_r, len(list_r))
                                    # print(row1[n][1] + ' ' + row2[n][1] + ' ' + row3[n][1], row1[n][0])

                                    wtf = random.randint(1, len(list_r))
                                    # print(wtf, list_r[wtf-1])
                                    writer.writerow([row1[n][0], list[list_r[wtf - 1]]])

                            elif row1[n] != row2[n]  and row3[n] != row2[n] and row1[n] != row3[n]:
                                n3 += 1
                                #print(row1[n][0] +' '+ row1[n][1] +' '+ row2[n][1] +' '+ row3[n][1])
                                a = list.index(row1[n][1])
                                b = list.index(row2[n][1])
                                c = list.index(row3[n][1])
                                aa = row11[n][a]
                                bb = row22[n][b]
                                cc = row33[n][c]
                                #print(a, b, c, aa, bb, cc)

                                maxXX = max(aa,bb,cc)


                                if aa == bb and aa == cc and bb == cc:
                                    # print(a, b, c, aa, bb, cc)

                                    # print(row1[n][0] + ' ' + row1[n][1] + ' ' + row2[n][1] + ' ' + row3[n][1])
                                    # print(a, b, c, aa, bb, cc)

                                    aaa = float(aa) / (float(row11[n][0]) + float(row11[n][1]) + float(row11[n][2]) + float(
                                        row11[n][3]) + float(row11[n][4]) + float(row11[n][5]) + float(row11[n][6]) + float(
                                        row11[n][7]) + float(row11[n][8]) + float(row11[n][9]) + float(
                                        row11[n][10]) + float(
                                        row11[n][11]) + float(row11[n][12]) + float(row11[n][13]) + float(row11[n][14]))
                                    bbb = float(bb) / (
                                            float(row22[n][0]) + float(row22[n][1]) + float(row22[n][2]) + float(
                                        row22[n][3]) + float(row22[n][4]) + float(row22[n][5]) + float(
                                        row22[n][6]) + float(row22[n][7]) + float(row22[n][8]) + float(
                                        row22[n][9]) + float(row22[n][10]) + float(row22[n][11]) + float(
                                        row22[n][12]) + float(row22[n][13]) + float(row22[n][14]))
                                    ccc = float(cc) / (
                                            float(row33[n][0]) + float(row33[n][1]) + float(row33[n][2]) + float(
                                        row33[n][3]) + float(row33[n][4]) + float(row33[n][5]) + float(
                                        row33[n][6]) + float(row33[n][7]) + float(row33[n][8]) + float(
                                        row33[n][9]) + float(row33[n][10]) + float(row33[n][11]) + float(
                                        row33[n][12]) + float(row33[n][13]) + float(row33[n][14]))

                                    # print(aaa,bbb, ccc)

                                    axb = float(row11[n][b]) / (
                                                float(row11[n][0]) + float(row11[n][1]) + float(row11[n][2]) + float(
                                            row11[n][3]) + float(row11[n][4]) + float(row11[n][5]) + float(
                                            row11[n][6]) + float(
                                            row11[n][7]) + float(row11[n][8]) + float(row11[n][9]) + float(
                                            row11[n][10]) + float(
                                            row11[n][11]) + float(row11[n][12]) + float(row11[n][13]) + float(row11[n][14]))
                                    axc = float(row11[n][c]) / (
                                                float(row11[n][0]) + float(row11[n][1]) + float(row11[n][2]) + float(
                                            row11[n][3]) + float(row11[n][4]) + float(row11[n][5]) + float(
                                            row11[n][6]) + float(
                                            row11[n][7]) + float(row11[n][8]) + float(row11[n][9]) + float(
                                            row11[n][10]) + float(
                                            row11[n][11]) + float(row11[n][12]) + float(row11[n][13]) + float(row11[n][14]))
                                    bxa = float(row22[n][a]) / (
                                            float(row22[n][0]) + float(row22[n][1]) + float(row22[n][2]) + float(
                                        row22[n][3]) + float(row22[n][4]) + float(row22[n][5]) + float(
                                        row22[n][6]) + float(row22[n][7]) + float(row22[n][8]) + float(
                                        row22[n][9]) + float(row22[n][10]) + float(row22[n][11]) + float(
                                        row22[n][12]) + float(row22[n][13]) + float(row22[n][14]))
                                    bxc = float(row22[n][c]) / (
                                            float(row22[n][0]) + float(row22[n][1]) + float(row22[n][2]) + float(
                                        row22[n][3]) + float(row22[n][4]) + float(row22[n][5]) + float(
                                        row22[n][6]) + float(row22[n][7]) + float(row22[n][8]) + float(
                                        row22[n][9]) + float(row22[n][10]) + float(row22[n][11]) + float(
                                        row22[n][12]) + float(row22[n][13]) + float(row22[n][14]))
                                    cxa = float(row33[n][a]) / (
                                            float(row33[n][0]) + float(row33[n][1]) + float(row33[n][2]) + float(
                                        row33[n][3]) + float(row33[n][4]) + float(row33[n][5]) + float(
                                        row33[n][6]) + float(row33[n][7]) + float(row33[n][8]) + float(
                                        row33[n][9]) + float(row33[n][10]) + float(row33[n][11]) + float(
                                        row33[n][12]) + float(row33[n][13]) + float(row33[n][14]))
                                    cxb = float(row33[n][b]) / (
                                            float(row33[n][0]) + float(row33[n][1]) + float(row33[n][2]) + float(
                                        row33[n][3]) + float(row33[n][4]) + float(row33[n][5]) + float(
                                        row33[n][6]) + float(row33[n][7]) + float(row33[n][8]) + float(
                                        row33[n][9]) + float(row33[n][10]) + float(row33[n][11]) + float(
                                        row33[n][12]) + float(row33[n][13]) + float(row33[n][14]))
                                    # print(aaa-axb,aaa-axc,bbb-bxa,bbb-bxc,ccc-cxa,ccc-cxb)

                                    max_value = max(aaa - axb, aaa - axc, bbb - bxa, bbb - bxc, ccc - cxa, ccc - cxb)
                                    # print(max_value)

                                    if aaa - axb == aaa - axc == bbb - bxa == bbb - bxc == ccc - cxa == ccc - cxb:
                                        wtf = random.randint(1, 3)
                                        if wtf == 1:
                                            writer.writerow([row1[n][0], row1[n][1]])
                                            n33 += 1
                                        elif wtf == 2:
                                            writer.writerow([row1[n][0], row2[n][1]])
                                            n33 += 1
                                        elif wtf == 3:
                                            writer.writerow([row1[n][0], row3[n][1]])
                                            n33 += 1
                                    elif max_value == aaa - axb or max_value == aaa - axc:
                                        writer.writerow([row1[n][0], row1[n][1]])
                                        n33 += 1
                                    elif max_value == bbb - bxa or max_value == bbb - bxc:
                                        writer.writerow([row2[n][0], row2[n][1]])
                                        n33 += 1
                                    elif max_value == ccc - cxa or max_value == ccc - cxb:
                                        writer.writerow([row3[n][0], row3[n][1]])
                                        n33 += 1

                                elif aa > bb and aa > cc:
                                    writer.writerow([row1[n][0], row1[n][1]])
                                    n333+=1

                                elif bb > aa and bb > cc:
                                    writer.writerow([row2[n][0], row2[n][1]])
                                    n333+=1

                                elif cc > aa and cc > bb:
                                    writer.writerow([row3[n][0], row3[n][1]])
                                    n333+=1

                                elif maxXX==aa==bb:
                                    aaa = float(aa) / (
                                                float(row11[n][0]) + float(row11[n][1]) + float(row11[n][2]) + float(
                                            row11[n][3]) + float(row11[n][4]) + float(row11[n][5]) + float(
                                            row11[n][6]) + float(
                                            row11[n][7]) + float(row11[n][8]) + float(row11[n][9]) + float(
                                            row11[n][10]) + float(
                                            row11[n][11]) + float(row11[n][12]) + float(row11[n][13]) + float(
                                            row11[n][14]))
                                    bbb = float(bb) / (
                                            float(row22[n][0]) + float(row22[n][1]) + float(row22[n][2]) + float(
                                        row22[n][3]) + float(row22[n][4]) + float(row22[n][5]) + float(
                                        row22[n][6]) + float(row22[n][7]) + float(row22[n][8]) + float(
                                        row22[n][9]) + float(row22[n][10]) + float(row22[n][11]) + float(
                                        row22[n][12]) + float(row22[n][13]) + float(row22[n][14]))
                                    ccc = float(cc) / (
                                            float(row33[n][0]) + float(row33[n][1]) + float(row33[n][2]) + float(
                                        row33[n][3]) + float(row33[n][4]) + float(row33[n][5]) + float(
                                        row33[n][6]) + float(row33[n][7]) + float(row33[n][8]) + float(
                                        row33[n][9]) + float(row33[n][10]) + float(row33[n][11]) + float(
                                        row33[n][12]) + float(row33[n][13]) + float(row33[n][14]))

                                    # print(aaa,bbb, ccc)

                                    axb = float(row11[n][b]) / (
                                            float(row11[n][0]) + float(row11[n][1]) + float(row11[n][2]) + float(
                                        row11[n][3]) + float(row11[n][4]) + float(row11[n][5]) + float(
                                        row11[n][6]) + float(
                                        row11[n][7]) + float(row11[n][8]) + float(row11[n][9]) + float(
                                        row11[n][10]) + float(
                                        row11[n][11]) + float(row11[n][12]) + float(row11[n][13]) + float(row11[n][14]))
                                    axc = float(row11[n][c]) / (
                                            float(row11[n][0]) + float(row11[n][1]) + float(row11[n][2]) + float(
                                        row11[n][3]) + float(row11[n][4]) + float(row11[n][5]) + float(
                                        row11[n][6]) + float(
                                        row11[n][7]) + float(row11[n][8]) + float(row11[n][9]) + float(
                                        row11[n][10]) + float(
                                        row11[n][11]) + float(row11[n][12]) + float(row11[n][13]) + float(row11[n][14]))
                                    bxa = float(row22[n][a]) / (
                                            float(row22[n][0]) + float(row22[n][1]) + float(row22[n][2]) + float(
                                        row22[n][3]) + float(row22[n][4]) + float(row22[n][5]) + float(
                                        row22[n][6]) + float(row22[n][7]) + float(row22[n][8]) + float(
                                        row22[n][9]) + float(row22[n][10]) + float(row22[n][11]) + float(
                                        row22[n][12]) + float(row22[n][13]) + float(row22[n][14]))
                                    bxc = float(row22[n][c]) / (
                                            float(row22[n][0]) + float(row22[n][1]) + float(row22[n][2]) + float(
                                        row22[n][3]) + float(row22[n][4]) + float(row22[n][5]) + float(
                                        row22[n][6]) + float(row22[n][7]) + float(row22[n][8]) + float(
                                        row22[n][9]) + float(row22[n][10]) + float(row22[n][11]) + float(
                                        row22[n][12]) + float(row22[n][13]) + float(row22[n][14]))
                                    cxa = float(row33[n][a]) / (
                                            float(row33[n][0]) + float(row33[n][1]) + float(row33[n][2]) + float(
                                        row33[n][3]) + float(row33[n][4]) + float(row33[n][5]) + float(
                                        row33[n][6]) + float(row33[n][7]) + float(row33[n][8]) + float(
                                        row33[n][9]) + float(row33[n][10]) + float(row33[n][11]) + float(
                                        row33[n][12]) + float(row33[n][13]) + float(row33[n][14]))
                                    cxb = float(row33[n][b]) / (
                                            float(row33[n][0]) + float(row33[n][1]) + float(row33[n][2]) + float(
                                        row33[n][3]) + float(row33[n][4]) + float(row33[n][5]) + float(
                                        row33[n][6]) + float(row33[n][7]) + float(row33[n][8]) + float(
                                        row33[n][9]) + float(row33[n][10]) + float(row33[n][11]) + float(
                                        row33[n][12]) + float(row33[n][13]) + float(row33[n][14]))
                                    # print(aaa-axb,aaa-axc,bbb-bxa,bbb-bxc,ccc-cxa,ccc-cxb)

                                    max_value = max(aaa - axb, aaa - axc, bbb - bxa, bbb - bxc, ccc - cxa, ccc - cxb)
                                    # print(max_value)

                                    if aaa - axb == aaa - axc == bbb - bxa == bbb - bxc == ccc - cxa == ccc - cxb:
                                        wtf = random.randint(1, 2)
                                        if wtf == 1:
                                            writer.writerow([row1[n][0], row1[n][1]])

                                        elif wtf == 2:
                                            writer.writerow([row2[n][0], row2[n][1]])

                                    elif max_value == aaa - axb or max_value == aaa - axc:
                                        writer.writerow([row1[n][0], row1[n][1]])
                                        n33 += 1
                                    elif max_value == bbb - bxa or max_value == bbb - bxc:
                                        writer.writerow([row2[n][0], row2[n][1]])
                                        n33 += 1
                                    elif max_value == ccc - cxa or max_value == ccc - cxb:
                                        wtf = random.randint(1, 2)
                                        if wtf == 1:
                                            writer.writerow([row1[n][0], row1[n][1]])
                                        elif wtf == 2:
                                            writer.writerow([row2[n][0], row2[n][1]])

                                elif maxXX==aa==cc:
                                    aaa = float(aa) / (
                                                float(row11[n][0]) + float(row11[n][1]) + float(row11[n][2]) + float(
                                            row11[n][3]) + float(row11[n][4]) + float(row11[n][5]) + float(
                                            row11[n][6]) + float(
                                            row11[n][7]) + float(row11[n][8]) + float(row11[n][9]) + float(
                                            row11[n][10]) + float(
                                            row11[n][11]) + float(row11[n][12]) + float(row11[n][13]) + float(
                                            row11[n][14]))
                                    bbb = float(bb) / (
                                            float(row22[n][0]) + float(row22[n][1]) + float(row22[n][2]) + float(
                                        row22[n][3]) + float(row22[n][4]) + float(row22[n][5]) + float(
                                        row22[n][6]) + float(row22[n][7]) + float(row22[n][8]) + float(
                                        row22[n][9]) + float(row22[n][10]) + float(row22[n][11]) + float(
                                        row22[n][12]) + float(row22[n][13]) + float(row22[n][14]))
                                    ccc = float(cc) / (
                                            float(row33[n][0]) + float(row33[n][1]) + float(row33[n][2]) + float(
                                        row33[n][3]) + float(row33[n][4]) + float(row33[n][5]) + float(
                                        row33[n][6]) + float(row33[n][7]) + float(row33[n][8]) + float(
                                        row33[n][9]) + float(row33[n][10]) + float(row33[n][11]) + float(
                                        row33[n][12]) + float(row33[n][13]) + float(row33[n][14]))

                                    # print(aaa,bbb, ccc)

                                    axb = float(row11[n][b]) / (
                                            float(row11[n][0]) + float(row11[n][1]) + float(row11[n][2]) + float(
                                        row11[n][3]) + float(row11[n][4]) + float(row11[n][5]) + float(
                                        row11[n][6]) + float(
                                        row11[n][7]) + float(row11[n][8]) + float(row11[n][9]) + float(
                                        row11[n][10]) + float(
                                        row11[n][11]) + float(row11[n][12]) + float(row11[n][13]) + float(row11[n][14]))
                                    axc = float(row11[n][c]) / (
                                            float(row11[n][0]) + float(row11[n][1]) + float(row11[n][2]) + float(
                                        row11[n][3]) + float(row11[n][4]) + float(row11[n][5]) + float(
                                        row11[n][6]) + float(
                                        row11[n][7]) + float(row11[n][8]) + float(row11[n][9]) + float(
                                        row11[n][10]) + float(
                                        row11[n][11]) + float(row11[n][12]) + float(row11[n][13]) + float(row11[n][14]))
                                    bxa = float(row22[n][a]) / (
                                            float(row22[n][0]) + float(row22[n][1]) + float(row22[n][2]) + float(
                                        row22[n][3]) + float(row22[n][4]) + float(row22[n][5]) + float(
                                        row22[n][6]) + float(row22[n][7]) + float(row22[n][8]) + float(
                                        row22[n][9]) + float(row22[n][10]) + float(row22[n][11]) + float(
                                        row22[n][12]) + float(row22[n][13]) + float(row22[n][14]))
                                    bxc = float(row22[n][c]) / (
                                            float(row22[n][0]) + float(row22[n][1]) + float(row22[n][2]) + float(
                                        row22[n][3]) + float(row22[n][4]) + float(row22[n][5]) + float(
                                        row22[n][6]) + float(row22[n][7]) + float(row22[n][8]) + float(
                                        row22[n][9]) + float(row22[n][10]) + float(row22[n][11]) + float(
                                        row22[n][12]) + float(row22[n][13]) + float(row22[n][14]))
                                    cxa = float(row33[n][a]) / (
                                            float(row33[n][0]) + float(row33[n][1]) + float(row33[n][2]) + float(
                                        row33[n][3]) + float(row33[n][4]) + float(row33[n][5]) + float(
                                        row33[n][6]) + float(row33[n][7]) + float(row33[n][8]) + float(
                                        row33[n][9]) + float(row33[n][10]) + float(row33[n][11]) + float(
                                        row33[n][12]) + float(row33[n][13]) + float(row33[n][14]))
                                    cxb = float(row33[n][b]) / (
                                            float(row33[n][0]) + float(row33[n][1]) + float(row33[n][2]) + float(
                                        row33[n][3]) + float(row33[n][4]) + float(row33[n][5]) + float(
                                        row33[n][6]) + float(row33[n][7]) + float(row33[n][8]) + float(
                                        row33[n][9]) + float(row33[n][10]) + float(row33[n][11]) + float(
                                        row33[n][12]) + float(row33[n][13]) + float(row33[n][14]))
                                    # print(aaa-axb,aaa-axc,bbb-bxa,bbb-bxc,ccc-cxa,ccc-cxb)

                                    max_value = max(aaa - axb, aaa - axc, bbb - bxa, bbb - bxc, ccc - cxa, ccc - cxb)
                                    # print(max_value)

                                    if aaa - axb == aaa - axc == bbb - bxa == bbb - bxc == ccc - cxa == ccc - cxb:
                                        wtf = random.randint(1, 2)
                                        if wtf == 1:
                                            writer.writerow([row1[n][0], row1[n][1]])
                                            n33 += 1
                                        elif wtf == 2:
                                            writer.writerow([row1[n][0], row3[n][1]])
                                            n33 += 1

                                    elif max_value == aaa - axb or max_value == aaa - axc:
                                        writer.writerow([row1[n][0], row1[n][1]])
                                        n33 += 1
                                    elif max_value == bbb - bxa or max_value == bbb - bxc:
                                        wtf = random.randint(1, 2)
                                        if wtf == 1:
                                            writer.writerow([row1[n][0], row1[n][1]])
                                        elif wtf == 2:
                                            writer.writerow([row2[n][0], row3[n][1]])
                                    elif max_value == ccc - cxa or max_value == ccc - cxb:
                                        writer.writerow([row3[n][0], row3[n][1]])
                                        n33 += 1

                                elif maxXX==bb==cc:
                                    aaa = float(aa) / (
                                                float(row11[n][0]) + float(row11[n][1]) + float(row11[n][2]) + float(
                                            row11[n][3]) + float(row11[n][4]) + float(row11[n][5]) + float(
                                            row11[n][6]) + float(
                                            row11[n][7]) + float(row11[n][8]) + float(row11[n][9]) + float(
                                            row11[n][10]) + float(
                                            row11[n][11]) + float(row11[n][12]) + float(row11[n][13]) + float(
                                            row11[n][14]))
                                    bbb = float(bb) / (
                                            float(row22[n][0]) + float(row22[n][1]) + float(row22[n][2]) + float(
                                        row22[n][3]) + float(row22[n][4]) + float(row22[n][5]) + float(
                                        row22[n][6]) + float(row22[n][7]) + float(row22[n][8]) + float(
                                        row22[n][9]) + float(row22[n][10]) + float(row22[n][11]) + float(
                                        row22[n][12]) + float(row22[n][13]) + float(row22[n][14]))
                                    ccc = float(cc) / (
                                            float(row33[n][0]) + float(row33[n][1]) + float(row33[n][2]) + float(
                                        row33[n][3]) + float(row33[n][4]) + float(row33[n][5]) + float(
                                        row33[n][6]) + float(row33[n][7]) + float(row33[n][8]) + float(
                                        row33[n][9]) + float(row33[n][10]) + float(row33[n][11]) + float(
                                        row33[n][12]) + float(row33[n][13]) + float(row33[n][14]))

                                    # print(aaa,bbb, ccc)

                                    axb = float(row11[n][b]) / (
                                            float(row11[n][0]) + float(row11[n][1]) + float(row11[n][2]) + float(
                                        row11[n][3]) + float(row11[n][4]) + float(row11[n][5]) + float(
                                        row11[n][6]) + float(
                                        row11[n][7]) + float(row11[n][8]) + float(row11[n][9]) + float(
                                        row11[n][10]) + float(
                                        row11[n][11]) + float(row11[n][12]) + float(row11[n][13]) + float(row11[n][14]))
                                    axc = float(row11[n][c]) / (
                                            float(row11[n][0]) + float(row11[n][1]) + float(row11[n][2]) + float(
                                        row11[n][3]) + float(row11[n][4]) + float(row11[n][5]) + float(
                                        row11[n][6]) + float(
                                        row11[n][7]) + float(row11[n][8]) + float(row11[n][9]) + float(
                                        row11[n][10]) + float(
                                        row11[n][11]) + float(row11[n][12]) + float(row11[n][13]) + float(row11[n][14]))
                                    bxa = float(row22[n][a]) / (
                                            float(row22[n][0]) + float(row22[n][1]) + float(row22[n][2]) + float(
                                        row22[n][3]) + float(row22[n][4]) + float(row22[n][5]) + float(
                                        row22[n][6]) + float(row22[n][7]) + float(row22[n][8]) + float(
                                        row22[n][9]) + float(row22[n][10]) + float(row22[n][11]) + float(
                                        row22[n][12]) + float(row22[n][13]) + float(row22[n][14]))
                                    bxc = float(row22[n][c]) / (
                                            float(row22[n][0]) + float(row22[n][1]) + float(row22[n][2]) + float(
                                        row22[n][3]) + float(row22[n][4]) + float(row22[n][5]) + float(
                                        row22[n][6]) + float(row22[n][7]) + float(row22[n][8]) + float(
                                        row22[n][9]) + float(row22[n][10]) + float(row22[n][11]) + float(
                                        row22[n][12]) + float(row22[n][13]) + float(row22[n][14]))
                                    cxa = float(row33[n][a]) / (
                                            float(row33[n][0]) + float(row33[n][1]) + float(row33[n][2]) + float(
                                        row33[n][3]) + float(row33[n][4]) + float(row33[n][5]) + float(
                                        row33[n][6]) + float(row33[n][7]) + float(row33[n][8]) + float(
                                        row33[n][9]) + float(row33[n][10]) + float(row33[n][11]) + float(
                                        row33[n][12]) + float(row33[n][13]) + float(row33[n][14]))
                                    cxb = float(row33[n][b]) / (
                                            float(row33[n][0]) + float(row33[n][1]) + float(row33[n][2]) + float(
                                        row33[n][3]) + float(row33[n][4]) + float(row33[n][5]) + float(
                                        row33[n][6]) + float(row33[n][7]) + float(row33[n][8]) + float(
                                        row33[n][9]) + float(row33[n][10]) + float(row33[n][11]) + float(
                                        row33[n][12]) + float(row33[n][13]) + float(row33[n][14]))
                                    # print(aaa-axb,aaa-axc,bbb-bxa,bbb-bxc,ccc-cxa,ccc-cxb)

                                    max_value = max(aaa - axb, aaa - axc, bbb - bxa, bbb - bxc, ccc - cxa, ccc - cxb)
                                    # print(max_value)

                                    if aaa - axb == aaa - axc == bbb - bxa == bbb - bxc == ccc - cxa == ccc - cxb:
                                        wtf = random.randint(1, 2)
                                        if wtf == 1:
                                            writer.writerow([row1[n][0], row2[n][1]])
                                            n33 += 1
                                        elif wtf == 2:
                                            writer.writerow([row1[n][0], row3[n][1]])
                                            n33 += 1

                                    elif max_value == aaa - axb or max_value == aaa - axc:
                                        wtf = random.randint(1, 2)
                                        if wtf == 1:
                                            writer.writerow([row1[n][0], row2[n][1]])
                                        elif wtf == 2:
                                            writer.writerow([row2[n][0], row3[n][1]])
                                    elif max_value == bbb - bxa or max_value == bbb - bxc:
                                        writer.writerow([row2[n][0], row2[n][1]])
                                        n33 += 1
                                    elif max_value == ccc - cxa or max_value == ccc - cxb:
                                        writer.writerow([row3[n][0], row3[n][1]])
                                        n33 += 1

                            elif row1[n] != row2[n] or row3[n] != row2[n] or row1[n] != row3[n]:
                                #print(row1[n][1] + ' ' + row2[n][1] + ' ' + row3[n][1], row1[n][0])

                                a = list.index(row1[n][1])
                                b = list.index(row2[n][1])
                                c = list.index(row3[n][1])
                                aa = row11[n][a]
                                bb = row22[n][b]
                                cc = row33[n][c]
                                # print(a, b, c, aa, bb, cc)
                                '''
                                maxXX = max(aa, bb, cc)                                

                                list_of_word = [row1[n][1], row2[n][1], row3[n][1]]
                                cx = Counter(list_of_word)
                                ccx = cx.most_common(1)[0]
                                #print(cc[0])
                                #writer.writerow([row1[n][0], ccx[0]])
                                writer.writerow([row1[n][0], row3[n][1]])
                                #print(ccx)
                                '''

                                aaa = float(aa) / (float(row11[n][0]) + float(row11[n][1]) + float(row11[n][2]) + float(
                                    row11[n][3]) + float(row11[n][4]) + float(row11[n][5]) + float(row11[n][6]) + float(
                                    row11[n][7]) + float(row11[n][8]) + float(row11[n][9]) + float(
                                    row11[n][10]) + float(
                                    row11[n][11]) + float(row11[n][12]) + float(row11[n][13]) + float(row11[n][14]))
                                bbb = float(bb) / (
                                        float(row22[n][0]) + float(row22[n][1]) + float(row22[n][2]) + float(
                                    row22[n][3]) + float(row22[n][4]) + float(row22[n][5]) + float(
                                    row22[n][6]) + float(row22[n][7]) + float(row22[n][8]) + float(
                                    row22[n][9]) + float(row22[n][10]) + float(row22[n][11]) + float(
                                    row22[n][12]) + float(row22[n][13]) + float(row22[n][14]))
                                ccc = float(cc) / (
                                        float(row33[n][0]) + float(row33[n][1]) + float(row33[n][2]) + float(
                                    row33[n][3]) + float(row33[n][4]) + float(row33[n][5]) + float(
                                    row33[n][6]) + float(row33[n][7]) + float(row33[n][8]) + float(
                                    row33[n][9]) + float(row33[n][10]) + float(row33[n][11]) + float(
                                    row33[n][12]) + float(row33[n][13]) + float(row33[n][14]))

                                #max_n = max(aaa,bbb,ccc)

                                axb = float(row11[n][b]) / (
                                        float(row11[n][0]) + float(row11[n][1]) + float(row11[n][2]) + float(
                                    row11[n][3]) + float(row11[n][4]) + float(row11[n][5]) + float(
                                    row11[n][6]) + float(
                                    row11[n][7]) + float(row11[n][8]) + float(row11[n][9]) + float(
                                    row11[n][10]) + float(
                                    row11[n][11]) + float(row11[n][12]) + float(row11[n][13]) + float(row11[n][14]))
                                axc = float(row11[n][c]) / (
                                        float(row11[n][0]) + float(row11[n][1]) + float(row11[n][2]) + float(
                                    row11[n][3]) + float(row11[n][4]) + float(row11[n][5]) + float(
                                    row11[n][6]) + float(
                                    row11[n][7]) + float(row11[n][8]) + float(row11[n][9]) + float(
                                    row11[n][10]) + float(
                                    row11[n][11]) + float(row11[n][12]) + float(row11[n][13]) + float(row11[n][14]))
                                bxa = float(row22[n][a]) / (
                                        float(row22[n][0]) + float(row22[n][1]) + float(row22[n][2]) + float(
                                    row22[n][3]) + float(row22[n][4]) + float(row22[n][5]) + float(
                                    row22[n][6]) + float(row22[n][7]) + float(row22[n][8]) + float(
                                    row22[n][9]) + float(row22[n][10]) + float(row22[n][11]) + float(
                                    row22[n][12]) + float(row22[n][13]) + float(row22[n][14]))
                                bxc = float(row22[n][c]) / (
                                        float(row22[n][0]) + float(row22[n][1]) + float(row22[n][2]) + float(
                                    row22[n][3]) + float(row22[n][4]) + float(row22[n][5]) + float(
                                    row22[n][6]) + float(row22[n][7]) + float(row22[n][8]) + float(
                                    row22[n][9]) + float(row22[n][10]) + float(row22[n][11]) + float(
                                    row22[n][12]) + float(row22[n][13]) + float(row22[n][14]))
                                cxa = float(row33[n][a]) / (
                                        float(row33[n][0]) + float(row33[n][1]) + float(row33[n][2]) + float(
                                    row33[n][3]) + float(row33[n][4]) + float(row33[n][5]) + float(
                                    row33[n][6]) + float(row33[n][7]) + float(row33[n][8]) + float(
                                    row33[n][9]) + float(row33[n][10]) + float(row33[n][11]) + float(
                                    row33[n][12]) + float(row33[n][13]) + float(row33[n][14]))
                                cxb = float(row33[n][b]) / (
                                        float(row33[n][0]) + float(row33[n][1]) + float(row33[n][2]) + float(
                                    row33[n][3]) + float(row33[n][4]) + float(row33[n][5]) + float(
                                    row33[n][6]) + float(row33[n][7]) + float(row33[n][8]) + float(
                                    row33[n][9]) + float(row33[n][10]) + float(row33[n][11]) + float(
                                    row33[n][12]) + float(row33[n][13]) + float(row33[n][14]))
                                #print(a, b, c, aaa, bbb, ccc)
                                #print(row1[n][0] + ' ' + row1[n][1] + ' ' + row2[n][1] + ' ' + row3[n][1])
                                #print(aaa - axb, aaa - axc, bbb - bxa, bbb - bxc, ccc - cxa, ccc - cxb)
                                max_value = max(aaa - axb, aaa - axc, bbb - bxa, bbb - bxc, ccc - cxa, ccc - cxb)

                                if aaa - axb == aaa - axc == bbb - bxa == bbb - bxc == ccc - cxa == ccc - cxb:
                                    #maxXX = max(aa, bb, cc)
                                    list_of_word = [row1[n][1], row2[n][1], row3[n][1]]
                                    cx = Counter(list_of_word)
                                    ccx = cx.most_common(1)[0]
                                    #print(cc[0])
                                    writer.writerow([row1[n][0], ccx[0]])
                                elif max_value == aaa - axb or max_value == aaa - axc:
                                    writer.writerow([row2[n][0], row1[n][1]])
                                elif max_value == bbb - bxa or max_value == bbb - bxc:
                                    writer.writerow([row2[n][0], row2[n][1]])
                                elif max_value == ccc - cxa or max_value == ccc - cxb:
                                    writer.writerow([row3[n][0], row3[n][1]])


                        #list = ['banana', 'bareland', 'carrot', 'corn', 'dragonfruit', 'garlic', 'guava', 'bareland', 'peanut', 'pineapple', 'pumpkin', 'rice', 'soybean', 'sugarcane', 'tomato']


                        print(n1, n2 , n3, n1+n2+n3-1)





'''
跑出三個純粹 class分數的 log
先讀CSV看不同 2/3 一樣 就直接取多
1/3 就讀class 看誰高
'''
