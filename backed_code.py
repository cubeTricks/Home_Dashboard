
import sqlite3
import datetime
from datetime import date
import shutil
import os
import webbrowser

tmp_table_for_calculations=[]
conn = sqlite3.connect('test.db')
print ("Opened database successfully")
cursor = conn.execute("SELECT q.item_no,q.item_name,q.start_date,q.initial_quantity,d.depriciation_factor from q2 q ,depriciation_1 d where q.item_no=d.item_no ")
for row in cursor:
   tmp_table_for_calculations.append(row)
   
conn.close()


for i in tmp_table_for_calculations:
    print(i)
'''

for i in tmp_table_for_calculations:
    format_str = '%d/%m/%Y' # The format
    datetime_obj = datetime.datetime.strptime(i[0], format_str)
    elapsed_days=date.today()-datetime_obj.date()
    print(elapsed_days.days)
'''    
    
tmp_output_table=[]

for i in tmp_table_for_calculations:
    tmp_table_row=[]
    tmp_table_row.append(i[0])
    tmp_table_row.append(i[1])
    format_str = '%d/%m/%Y' # The format
    datetime_obj = datetime.datetime.strptime(i[2], format_str)
    elapsed_days=date.today()-datetime_obj.date()
    remaining_quantity=i[3]-(i[4]*elapsed_days.days)
    tmp_table_row.append(remaining_quantity)
    tmp_table_row_html=''
    if remaining_quantity<500 and remaining_quantity>=200:
        tmp_table_row_html='<tr><td>'+str(i[0])+'</td><td>'+str(i[1])+'</td><td style="background-color:yellow" >'+str(remaining_quantity)+'</td></tr>'
    elif remaining_quantity<200:
        tmp_table_row_html='<tr><td>'+str(i[0])+'</td><td>'+str(i[1])+'</td><td style="background-color:red" >'+str(remaining_quantity)+'</td></tr>'
    elif remaining_quantity>=500:
        tmp_table_row_html='<tr><td>'+str(i[0])+'</td><td>'+str(i[1])+'</td><td style="background-color:green" >'+str(remaining_quantity)+'</td></tr>'
    tmp_output_table.append(tmp_table_row_html)
print(tmp_output_table)
    

os.chdir('.\dashboard\\templates')
# use copyfile()
f= open("board.html","w+")
shutil.copyfile('deafult_template.txt','board.html')
f.close()
f= open("board.html","a+")
for i in tmp_output_table:
    f.write(i)
f.write('</table></body></html>')
f.close()


webbrowser.open("board.html")
print('page_opened')
