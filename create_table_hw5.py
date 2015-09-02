import csv
import os

def create_textfile(schema_name, csv_files, table_names):

    """
    head, tail = os.path.split(filename)
    f_output = os.path.splitext(tail)[0]
    print f_output
    f_out = open( f_output+'.sql', "w")
    """
    
    f_out = open('insert.sql', "w")


    for i in range( len(csv_files) ): #per csv file
        
        with open(csv_files[i], 'r') as f:
            #f.readline() #header
            reader = list(csv.reader(f))
            cols = len( reader[0] )
            #print cols

            header = [] #store all years
            
            for idx, row in enumerate(reader): #for each row
                 
                if idx == 0: #header
                    for i in range(1, cols):
                        header.append(row[i])
                        
                else: #country rows
                    row[0] = row[0].replace("'", "''") #escape apostrophe
                    for i in range(1, cols): #each column is one insert statement
                        try:
                            if row[i].strip() and row[i] is not '-': #check for a blank string or '-'
                                first_line = "\ninsert into " + schema_name + "." + table_name + '\n' #insert a row into table table_name
                                #print first_line
                                f_out.write(first_line)

                                values_string = "values('" + row[0] + "'," + header[i-1] + ", " + row[i] + ");\n"
                                f_out.write(values_string)
                        except:
                            print "some error???\n\n\n"

    f_out.close()

"""
Main
"""
repeat = 1
          
while repeat == 1:
    schema_name = raw_input("Please input a schema name or 'q' to quit: ")
    
    if schema_name == 'q':
            break
        
    repeat_csv = 1
    csv_files = [] #list of csv files to parse
    table_names = [] #list of table names per csv file
    while repeat_csv == 1:
      print
      file_name = raw_input("Please specify csv file name or 'c' to continue: ")
      if file_name == "c":
          break
      
      
      table_name = raw_input("Please specify a table name or 'c' to continue: ")
      if table_name == "c":
          break
        
      csv_files.append(file_name)
      table_names.append(table_name)
      
    create_textfile(schema_name, csv_files, table_names)


    print
    print "**************Finished creating new insert file*******************"
    print
    
