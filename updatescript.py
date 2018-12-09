import git
	
inputFile = open('/home/pi/webhooks.tuffing.co.nz/webhooks-flask/queue.txt', 'r+')
repos = inputFile.read().strip().split('\n')
inputFile.truncate(0)
inputFile.close()


github = GITPATH = '/home/logan/projects/%s'
GITURL = 'git@github.com:tuffing/%s.git'


for repo in repos: 
	#update local repo from it's source
	g = git.cmd.Git('/home/logan/projects/%s' % repo)
	g.pull()

	g.push('git@github.com:tuffing/%s.git' % repo)