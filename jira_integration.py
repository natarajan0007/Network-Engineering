from jira.client import JIRA
import getpass
from prettytable import PrettyTable

password=getpass.getpass("Please Enter the password:")
options = {'server': 'https://workflow.advisory.com'}
jira = JIRA(options, basic_auth=('muthun', password)) 
abc =jira.search_issues('project = ETCCB AND "Business Unit Impacted" = "ABC Admin" AND "Change Category" = "Network/Infrastructure"  AND status = Unreviewed')


for xyz in abc:
	print xyz
	issue = jira.issue(xyz)
	project = issue.fields.project.key             # Project Name
	summary = issue.fields.summary                 # Description of the change
	assignee = issue.fields.assignee               # Owner of the change
	created = issue.fields.created                 # Created Time
	time = issue.fields.timeestimate               # timestamp
	issuetype = issue.fields.issuetype.name        
	displayname = issue.fields.reporter.displayName # reporter name
	t = PrettyTable(['project','summary','assignee','create','time','issuetype','displayname'])
	t.add_row([project,summary,assignee,created,time,issuetype,displayname])
	print t
    
	
