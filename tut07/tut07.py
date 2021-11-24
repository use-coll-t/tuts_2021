import os

import pandas as pd


dict_ltp={}

main_dict={}



def check(submitted_dict,registered_dict,roll):

	if roll in registered_dict:

		temp=registered_dict[roll].copy()

		n=len(temp)

		s=[]

		m=len(submitted_dict)

		if(n!=m):

			

			for i in temp:

				x=dict_ltp[i]

	

				if submitted_dict.count(i)!=x[0][1]:

					if temp.count(i)!=x[0][1]:

						diff=x[0][1]-temp.count(i)

						while diff>0:

							s.append(i)

							diff-=1

				s.append(i)

			

			for j in submitted_dict:

				x=dict_ltp[j]

				if j in s:

					s.remove(j)

			if len(s)!=0:		

				if roll in main_dict:

					main_dict[roll].append(s)

				else:

					main_dict[roll]=[]

					main_dict[roll].append(s)

				return roll

	


def ltp_to_bits(s):

		count=0

		zeroes=0

		for k in range(len(s)):

			if((s[k])=='0'):

				zeroes+=1

			

		count=3-zeroes

		return count



def feedback_not_submitted():


	

	ltp_mapping_feedback_type = {1: 'lecture', 2: 'tutorial', 3:'practical'}

	output_file_name = "course_feedback_remaining.xlsx" 

	registered_file=pd.read_csv('course_registered_by_all_students.csv')

	registered_roll=registered_file['rollno'].values.tolist()

	registered_data=registered_file[['register_sem','schedule_sem','subno']].values.tolist()

	registered_sub=registered_file['subno'].values.tolist()

	

	unique_registered_roll=set(registered_roll)

	registered_dict={}

	

	i=0

	for k in registered_roll:

		if k in registered_dict:

			registered_dict[k].append(registered_sub[i])

		else:

			registered_dict[k]=[]

			registered_dict[k].append(registered_sub[i])

		

		i+=1

	

	i=0

	registered_data_dict={}

	for k in registered_sub:

		registered_data_dict[k]=[]

		registered_data_dict[k]=registered_data[i]

		i+=1


	

	submitted_file=pd.read_csv("course_feedback_submitted_by_students.csv")

	submitted_sub=submitted_file['course_code'].values.tolist()

	submitted_roll=submitted_file['stud_roll'].values.tolist()

	unique_submitted_roll=set(submitted_file)

	submitted_dict={}


	l=0

	for k in submitted_roll:

		if k in submitted_dict:

			submitted_dict[k].append(submitted_sub[l])

		else:

			submitted_dict[k]=[]

			submitted_dict[k].append(submitted_sub[l])

		l+=1


	

	info_file=pd.read_csv('studentinfo.csv')

	ltp_file=pd.read_csv('course_master_dont_open_in_excel.csv')

	

	ltp_list=ltp_file['ltp'].values.tolist()

	ltp_sub=ltp_file['subno'].values.tolist()

	

	



	l=0

	for k in ltp_sub:

		bits=ltp_to_bits(ltp_list[l])

		if k in dict_ltp:

			

			dict_ltp[k].append([ltp_list[l],bits])

		else:

			dict_ltp[k]=[]

			dict_ltp[k].append([ltp_list[l],bits])

		

		l+=1

	

	info_list=info_file[['Name','email','aemail','contact']].values.tolist()

	info_roll=info_file['Roll No'].values.tolist()


	dict_info={}


	l=0

	for k in info_roll:

		if k in dict_info:

			dict_info[k].append(info_list[l])

		else:

			dict_info[k]=[]

			dict_info[k].append(info_list[l])

		

		l+=1



	

	for i in unique_registered_roll:

		if i in submitted_dict:

			temp=check(submitted_dict[i],registered_dict,i)



	

	

	output_list=[[]]

	for i in main_dict:

		for j in main_dict[i]:

			

			

			for k in j:

				x=[]

				x.append(i)

				

			

				x.extend(registered_data_dict[k])

				p=dict_info[i]

				

				for l in range(4):

					x.append(p[0][l])

				

				output_list.append(x)

	print(output_list)

	


	output_data=pd.DataFrame(output_list,columns=['rollno','register_sem','schedule_sem','subno','Name','email','aemail','contact'])

	

	print(output_data.head())

output.to_excel(output_data)


feedback_not_submitted()