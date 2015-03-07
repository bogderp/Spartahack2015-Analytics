from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from urllib import urlopen
import json

# Create your views here.
typeFormURL = "https://api.typeform.com/v0/form/Zh7TEH?key=1b508a88a1331cf2c182cb136f6da1ebd880a299&completed=true"
jsonResults = ""
for i in urlopen(typeFormURL):
	jsonResults += str(i)
jsonResults = json.loads(jsonResults)
keys = {
	"Name": "textfield_4613064",
	"Email": "email_4613164",
	"Phone Number": "textfield_4613168",
	"Gender identity": "list_4613175_choice",
	"Month" : "number_4613245",
	"Day": "number_4613259",
	"Year": "number_4613260", 
	"T-Shirt size": "list_4613276_choice",
	"Where are you traveling from?": "textfield_4613285", 
	"What university do you currently attend?": "textfield_4613313", 
	"What is your major of study?": "textfield_4613318", 
	"Year in school": "list_4613345_choice", 
	"GitHub": "website_4613414",
	"LinkedIn": "website_4613464",
	"Personal Website": "website_4613469", 
	"Another cool link?": "website_4613471", 
	"Will this be your first hackathon?": "yesno_4613474", 
	"If no  what other hackathons have you attended?": "textarea_4613558", 
	"Are you willing to mentor?": "yesno_4613478", 
	"Technologies you're comfortable with": "list_4613658_choice_5343749",
	"Technologies you're comfortable with 1": "list_4613658_choice_5343750", 
	"Technologies you're comfortable with 2": "list_4613658_choice_5343751", 
	"Technologies you're comfortable with 3": "list_4613658_choice_5343752", 
	"Technologies you're comfortable with 4": "list_4613658_choice_5343753", 
	"Technologies you're comfortable with 5": "list_4613658_choice_5343754", 
	"Technologies you're comfortable with 6": "list_4613658_choice_5343755", 
	"Technologies you're comfortable with 7": "list_4613658_choice_5343756", 
	"Technologies you're comfortable with 8": "list_4613658_choice_5343757", 
	"Technologies you're comfortable with 9": "list_4613658_choice_5343758", 
	"Technologies you're comfortable with 10": "list_4613658_choice_5343759", 
	"Technologies you're comfortable with 11": "list_4613658_choice_5343760", 
	"Technologies you're comfortable with 12": "list_4613658_choice_5343761", 
	"Technologies you're comfortable with 13": "list_4613658_choice_5343762", 
	"Technologies you're comfortable with 14": "list_4613658_choice_5343763", 
	"Technologies you're comfortable with 15": "list_4613658_choice_5343764",
	"Technologies you're comfortable with 16": "list_4613658_choice_5343765", 
	"Technologies you're comfortable with 17": "list_4613658_choice_5343766", 
	"Technologies you're comfortable with 18": "list_4613658_choice_5343767", 
	"Technologies you're comfortable with 19": "list_4613658_choice_5343768", 
	"Technologies you're comfortable with 20": "list_4613658_choice_5343769", 
	"Technologies you're comfortable with 21": "list_4613658_choice_5343770", 
	"Technologies you're comfortable with 22": "list_4613658_choice_5343771", 
	"Technologies you're comfortable with 23": "list_4613658_choice_5343772", 
	"Technologies you're comfortable with 24": "list_4613658_choice_5343773", 
	"Technologies you're comfortable with 25": "list_4613658_choice_5343774", 
	"Is there any hardware you'd like to hack on?": "list_4613747_choice_5343880",
	"Is there any hardware you'd like to hack on? 1": "list_4613747_choice_5343881", 
	"Is there any hardware you'd like to hack on? 2": "list_4613747_choice_5343882",
	"Is there any hardware you'd like to hack on? 3": "list_4613747_choice_5343883", 
	"Is there any hardware you'd like to hack on? 4": "list_4613747_choice_5343884", 
	"Is there any hardware you'd like to hack on? 5": "list_4613747_choice_5343885", 
	"Is there any hardware you'd like to hack on? 6": "list_4613747_choice_5343886", 
	"Is there any hardware you'd like to hack on? 7": "list_4613747_choice_5343887", 
	"Is there any hardware you'd like to hack on? 8": "list_4613747_choice_5343888", 
	"Is there any other hardware you'd like to see at SpartaHack": "textarea_4613781", 
	"Link and/or description of your favorite project": "textarea_4613788", 
	"Do you need travel reimbursement to attend?": "yesno_4613836", 
	"Do you have an dietary restrictions we should be prepared to accommodate?": "textarea_4613853", 
	"Will you require any special accommodations?": "textarea_4613879", 
	"Please list the emails of any teammates you are applying with": "textarea_4613955"
}




def index(request):
	# college totals
	colleges = {}

	#birth month
	months = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}
	
	#distribution by age
	years = []

	youngest = [0,0,0]
	oldest = [12,31,9999]

	#rate of applications
	dayCounts = {};

	total = 0
	for i in jsonResults["responses"]:
		total += 1

		#for distribution by birth month
		months[i["answers"][keys["Month"]]] += 1;


		#find oldest and youngest
		if int(i["answers"][keys["Year"]]) < 100:
			i["answers"][keys["Year"]] = '19' + i["answers"][keys["Year"]];

		years.append(int(i["answers"][keys["Year"]]))

		if int(i["answers"][keys["Year"]]) <= oldest[2]:
			oldest[2] = int(i["answers"][keys["Year"]])
			if int(i["answers"][keys["Month"]]) <= oldest[1]:
				oldest[1] = int(i["answers"][keys["Month"]])
				if int(i["answers"][keys["Day"]]) <= oldest[0]:
					oldest[0] = int(i["answers"][keys["Day"]])
		
		if int(i["answers"][keys["Year"]]) >= youngest[2]:
			youngest[2] = int(i["answers"][keys["Year"]])
			if int(i["answers"][keys["Month"]]) >= youngest[1]:
				youngest[1] = int(i["answers"][keys["Month"]])
				if int(i["answers"][keys["Day"]]) >= youngest[0]:
					youngest[0] = int(i["answers"][keys["Day"]])

		college = i["answers"][keys["What university do you currently attend?"]].lower()
		college = college.replace(', ',' ')
		college = college.replace(' - ',' ')
		college = college.replace('-',' ')
		college = college.replace(' at ',' ')
		college = college.replace(' in ',' ')
		college = college.replace('  ',' ')

		college = college.replace('high school','highschool')
		college = college.replace('high schooler','highschool')
		college = college.replace('highschooler','highschool')
		college = college.replace('international academy east (hs)','highschool') 
		college = college.replace('still in hs','highschool')
		college = college.replace('still hs','highschool')
		if 'highschool' in college:
			college = 'highschool'
		college = college.replace('na\n','Not Applicable')
		college = college.replace('rutgers new brunswick','rutgers university')
		
		college = college.replace('michigan tech\n','michigan technological university')     #one off fix
		college = college.replace('michigan technological institute','michigan technological university')    #one off fix
		college = college.replace('depaul university chicago','depaul university') #one off fix
		college = college.replace('havard','harvard university')		#one off fix
		college = college.replace('technolog','technology')				#one off fix
		college = college.replace('technologyy','technology')			#one off fix
		college = college.replace('technologyical','technological')		#one off fix
		college = college.replace('the ohio','ohio')					#fuck that
		college = college.replace('the ','')							#additional fuck that
		college = college.replace('u of','university of')
		college = college.replace('michigan state','michigan state university')
		college = college.replace('msu','michigan state university')
		college = college.replace('um\n','university of michigan')
		college = college.replace('umich','university of michigan')
		college = college.replace('michigan\n','university of michigan')
		college = college.replace('university of michigan ann arbor','university of michigan')
		college = college.replace('university university','university')
		college = college.replace(' ann arbor','')
		college = college.rstrip().strip()
		try:
			colleges[college] += 1
		except KeyError:
			colleges[college] = 1

		dateTime = i['metadata']['date_submit'].split()
		date = dateTime[0]
		timeList = dateTime[1].split(':')
		hour = timeList[0]
		gender = i["answers"][keys["Gender identity"]];

		if date in dayCounts.keys():
			dayCounts[date][hour][0] +=1
			if gender == 'Male':
				dayCounts[date][hour][1] +=1
			elif gender == 'Female':
				dayCounts[date][hour][2] +=1
			else:
				dayCounts[date][hour][3] +=1
		else: 
			dayCounts[date]={'00':[0,0,0,0], '01':[0,0,0,0], '02':[0,0,0,0], '03':[0,0,0,0], '04':[0,0,0,0], 
							'05':[0,0,0,0], '06':[0,0,0,0], '07':[0,0,0,0], '08':[0,0,0,0], '09':[0,0,0,0], 
							'10':[0,0,0,0], '11':[0,0,0,0], '12':[0,0,0,0], '13':[0,0,0,0], '14':[0,0,0,0],
							'15':[0,0,0,0], '16':[0,0,0,0], '17':[0,0,0,0], '18':[0,0,0,0], '19':[0,0,0,0], 
							'20':[0,0,0,0], '21':[0,0,0,0], '22':[0,0,0,0], '23':[0,0,0,0]}
			dayCounts[date][hour][0] += 1
			if gender == 'Male':
				dayCounts[date][hour][1] +=1
			elif gender == 'Female':
				dayCounts[date][hour][2] +=1
			else:
				dayCounts[date][hour][3] +=1

	oldest = json.dumps(oldest)
	youngest = json.dumps(youngest)
	years = json.dumps(years)
	context = {"colleges":colleges, "total": total, "months": months, 'years':years, 'oldest':oldest, 'youngest': youngest, 'dayCounts': json.dumps(dayCounts)}
	return render(request, 'Visualization/index.html', context)

def table(request):
	tableResults= []
	rowModel= {}
	for question in keys.keys():
		rowModel[question] = "";

	for i in jsonResults["responses"]:
		row = rowModel
		for question in keys.keys():
			row[question] = i["answers"][keys[question]]

		tableResults.append(row);




	context = {'tableResults': json.dumps(tableResults)}
	return render(request, 'Visualization/table.html', context)






