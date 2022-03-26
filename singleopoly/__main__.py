import csv
def main():
    #creates properties
    with open('singleopoly\game\data\monopoly_properties_classic.txt') as file:
            properties = csv.reader(file, skipinitialspace=True)
            
            for row in properties:
                print (row)

            
 
if __name__ == "__main__":
    main()