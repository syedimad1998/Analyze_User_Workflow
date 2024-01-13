import csv, json, sys, os
#if you are not using utf-8 files, remove the next line
#sys.setdefaultencoding("UTF-8") #set the encode to utf8
#check if you pass the input file and output file
outputFile = open("test.csv", 'w') #load csv file
output = csv.writer(outputFile)
remove_words=['sessions','sessions_activities_details','sessions_activitySummary','sessions_activities_repeatActivityTimes','sessions_activities_pageTitle','sessions_activities_details']
header=[]
only_1_time=1
directory_in_str="/Users/syedimad/Downloads/user"
directory = os.fsencode(directory_in_str)
for file in os.listdir(directory):
    inputFile = open(file) #open json file
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        data = json.load(inputFile) #load json content
        dates=data["dates"]
         #create a csv.write
        #FIRST WE HAVE
        #type(dates[0]))<---AS DICT AND NOW WE CAN SUPPLY KEY TO ACCESS values
        #type(dates[0]['sessions']))<---now i get a list of values
        #type(dates[0]['sessions'][0]))<---now again i get a dictionary and i can access any key value pair
        #type(dates[0]['sessions'][0]['activities']))<- becoz activities is key hence this query returns its values which are dict
        #type(dates[0]['sessions'][0]['activities'][0]))<-converting into dict
        #type(dates[0]['sessions'][0]['activities'][0]['details'])<-and so on

        if only_1_time==1:
            header1=dates[0].keys()
            header2=dates[0]['sessions'][0].keys()
            header3=dates[0]['sessions'][0]['activitySummary'].keys()
            header4=dates[0]['sessions'][0]['activities'][0].keys()
            header5=dates[0]['sessions'][0]['activities'][0]['details'][0].keys()

            for x in header1:
                header.append(x)
            for x in header2:
                header.append("sessions_"+x)
            for x in header3:
                header.append("sessions_activitySummary"+x)
            for x in header4:
                header.append("sessions_activities_"+x)
            for x in header5:
                header.append("sessions_activities_details_"+x)


            #removing un wanted column
            for x in header:
                if x in remove_words:
                    header.remove(x)
            if 'sessions_activities' in header:
                header.remove('sessions_activities')
            if 'sessions_activities_details' in header:
                header.remove('sessions_activities_details')
            #appending at last
            header.append('sessions_activities_pageTitle')
            output.writerow(header)
            only_1_time=only_1_time+1

        for i in range(len(dates)):
            row=[]
            row1=dates[i].values()
            row2=dates[i]['sessions'][0].values()
            row3=dates[i]['sessions'][0]['activitySummary'].values()
            row4=dates[i]['sessions'][0]['activities'][0].values()
            row5=dates[i]['sessions'][0]['activities'][0]['details'][0].values()
            row1=list(row1)
            row2=list(row2)
            row3=list(row3)
            row4=list(row4)
            row5=list(row5)
            missed=row4[-1]
            #MODIFIED ROWS
            row1=row1[:-1]
            row2=row2[:-2]
            row4=row4[:-3]
            # for l in row3:
            #     if(int(l)>1):
            #         print(dates[i]['sessions'][0]['activities'][2].values())
            for l in range(int(row3[0])):
                row=[]
                if l==0:
                    for x in row1:
                        row.append(x)
                    for x in row2:
                        row.append(x)
                    for x in row3:
                        row.append(x)
                    for x in row4:
                        row.append(x)
                    for x in row5:
                        for z in x:
                            row.append(z)
                    row.append(missed)
                    output.writerow(row)
                    continue
                for x in row1:
                    row.append("")
                for x in row2:
                    row.append("")
                for x in row3:
                    row.append("")
                row4=dates[i]['sessions'][0]['activities'][l].values()
                row5=dates[i]['sessions'][0]['activities'][l]['details'][0].values()
                #modifying our ROW4
                row4=list(row4)
                row5=list(row5)
                row4=row4[:-3]

                for x in row4:
                    row.append(x)
                for x in row5:
                    for z in x:
                        row.append(z)
                row.append(missed)
                output.writerow(row)