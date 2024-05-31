
## CS131 Assignment 10
## Prajwal Bhandari
## March 2024


def find_2d(mat:list[list],item) ->int:
    for row in range(len(mat)):
        if mat[row][0]==item: #item needs to be the first or "0th" entry of a row
            return row
    return -1


def load_locations(fn:str) -> list[str]:
    if not isinstance(fn,str): 
        print("file name must be a string")
        return 

    file=open(fn,"r")
    list = []
    line=file.readline()
    line=file.readline()
    while line !="":
        line=line.replace("\n","")
        temp=line.split(",")
        list.append([int(temp[0]),temp[1]])
        line=file.readline()

    file.close()
    return list


def load_receipts(fn:str) -> list[list]:
    
    #open file, create a list, create a list of seen location IDs and read the first line
    file=open(fn,"r")
    list=[]
    seen_ids=[]
    line=file.readline()
    line=file.readline()    

    #reading through the document
    while line!="":
        #make the line into a list
        temp=line.split(',')

        #calculate spending for a given line:
        linetotal=float(temp[1])*(1+float(temp[2]))+float(temp[3])

        #if the first element isnt already in the seen list add it, since we want to get 
        #all data for a particular location into a single line in our outlist
        if find_2d(list,int(temp[0]))==-1: 
        #append the NEW location and the spending into the final list
            seen_ids.append(int(temp[0])) 
            list.append([int(temp[0]),linetotal])
        else: 
            list[find_2d(list,int(temp[0]))][1]+=linetotal

        #read the new line. 
        line=file.readline()

    file.close()
    return list 

def load_many_receipts(months:list[str],x) ->None:
    seen_ids=[]
    months_list=[]

    for i in range(len(months)):
        #open file, create a list, create a list of seen location IDs and read the first line
        file=open(months[i],"r")
        line=file.readline()
        line=file.readline()    

        #reading through the document
        while line!="":
            #make the line into a list
            temp=line.split(',')
            #calculate spending for a given line:
            linetotal=float(temp[1])*(1+float(temp[2]))+float(temp[3])

            #if the first element isnt already in the seen list add it, since we want to get 
            #all data for a particular location into a single line in our outlist
            if find_2d(months_list,int(temp[0]))==-1: 
            #append the NEW location and the spending into the final list
                seen_ids.append(int(temp[0])) 
                months_list.append([int(temp[0]),linetotal])
            else: 
                months_list[find_2d(months_list,int(temp[0]))][1]+=linetotal

            #read the new line. 
            line=file.readline()

        file.close()
    write_report("HW10\\report.txt",months_list,x)

    print(x)
    print(months_list)


def write_report(fn: str, data: list[list], places: list[list]) -> None:
    """Writes out the final report for this set of data.

    Args:
        fn (str): The filename to append to.
        data (list[list]): A 2D list of receipt record data.
        places (list[list]): A 2D list of identifiers and locations names.
    """
    if isinstance(places,str):
        places=load_locations(places)
    
    file=open(fn,"a")

    # Print the very front of the record
    file.write("****************************************\n")
    file.write("Total Records:" + str(len(data)) + "\n")

    # For each entry in the data list
    for i in range(len(data)):
        row = data[i]

        # Print out the name of the location this row represents
        file.write(places[find_2d(places, row[0])][1])

        # Print out the total amount spent at this location
        file.write("\t$" + str(row[1]) + "\n")
    file.close()


def main():
    # load_many_receipts(["HW10\\receipt_sep.csv", "HW10\\receipt_oct.csv","HW10\\receipt_nov.csv"],"HW10\\places.csv")

    print(load_locations("HW10\\places.csv"))
    print()
    print(load_receipts("HW10\\receipt_sep.csv"))
    print()
    print(load_receipts("HW10\\receipt_oct.csv"))
    print()
    print(load_receipts("HW10\\receipt_nov.csv"))
if __name__=="__main__":
    main()