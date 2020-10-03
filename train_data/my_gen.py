import os
import json
train_dir = "ICDAR2017_train"
for i in os.listdir(train_dir):
    if i.endswith(".txt"):
        output = []
        with open(train_dir+'/'+i,"r",encoding="utf-8-sig") as f:
            for line in f.readlines():
                try:
                    line1 = line.replace("\n","")
                    tmp = {}
                    tmp['transcription'] = line1.split('"')[-2]
                    squadsp = line1.split(',')[:8]
                    points = []
                    for j in range(0,len(squadsp),2):
                        points.append([int(squadsp[j]),int(squadsp[j+1])])
                    tmp['points'] = points
                    output.append(tmp)
                except Exception as e:
                    print(e)
                    print(i)
                    break
        with open("train_label.txt","a",encoding="utf-8") as ff:
            ff.write(train_dir+'/'+i[:-4]+'.jpg\t'+json.dumps(output)+'\n')