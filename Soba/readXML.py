import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

def TrainImg():
    with open("trainImg.txt","w") as file:

        file.write('{} 1\n'.format(image))
def OvlAnnotationFile():
    with open("AnnotationFile.txt","w") as file:
        file.write("#train.txt\n")
        with open("train.txt","r") as trainFile:
            line1=trainFile.read().splitlines()
            #print(line1)
            for line in line1:
                #if line[17] == '\n':
                 #   print("EOF")

                print(line)
                print(len(line))
                #line="Inari00000001.jpg"
                file.write("$DATASET_HOME/Inari/Images/"+line+" "+"$DATASET_HOME/Inari/Annotations/" + line.rstrip('.jpg') + ".txt\n")
        file.write("#val.txt\n")
        with open("val.txt","r") as trainFile:
            line1=trainFile.read().splitlines()
            #print(line1)
            for line in line1:
                #if line[17] == '\n':
                 #   print("EOF")

                print(line)
                print(len(line))
                #line="Inari00000001.jpg"
                file.write("$DATASET_HOME/Inari/Images/"+line+" "+"$DATASET_HOME/Inari/Annotations/" + line.rstrip('.jpg') + ".txt\n")
    return

def GenTestTextFiles(path):
    testCSV = "test_labels.csv"
    df = pd.read_csv(os.path.join(path + testCSV))
    # print(df['filename'])
    with open("val.txt", "w") as file:
        for eachFile in df['filename'].drop_duplicates():
            file.write(str(eachFile))
            file.write("\n")
    return

def GenTrainTextFiles(path):
    trainCSV="train_labels.csv"
    #testCSV="test_labels.csv"
    df=pd.read_csv(os.path.join(path+trainCSV))
    #print(df['filename'])
    with open("train.txt","w") as file:
        for eachFile in df['filename'].drop_duplicates():
            file.write(str(eachFile))
            file.write("\n")
    return

def ReadXML(path):
    xml_list=[]
    print(path)
    path = path + "/*.xml"
    print(glob.glob(path))

    import pdb;pdb.set_trace()
    for xml_file in glob.glob(path+"/*.xml"):
        tree = ET.parse(xml_file)
        root=tree.getroot()
        print(root)
        Imgname=root.find('filename').text
        txtFileName=str(Imgname).rstrip(".jpg")
        print(txtFileName)
        txtFileName="annotationsText\\"+txtFileName+".txt"
        #with open(os.path.join("annotationsText\\",txtFileName),"w") as file:
        with open(txtFileName, "w") as file:
            index=1
            file.write("# [label] [x1] [y1] [x2] [y2]")
            file.write("\n")
            for member in root.findall('object'):
                file.write('{}'.format(1)+" ")
                file.write('{}'.format(int(member[4][0].text))+" ")
                file.write('{}'.format(int(member[4][1].text))+" ")
                file.write('{}'.format(int(member[4][2].text))+" ")
                file.write('{}'.format(int(member[4][3].text))+"\n")
                index=index+1


def main():
    image_path = os.path.join(os.getcwd(),'/annotations')
    print(image_path)
    ReadXML(image_path)
    csv_path=os.path.join(os.getcwd(),'/data')
    GenTrainTextFiles(csv_path)
    GenTestTextFiles(csv_path)
    OvlAnnotationFile()
    print("XML Reading function ")

main()
