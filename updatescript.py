import git
	
inputFile = open('/home/pi/webhooks.tuffing.co.nz/webhooks-flask/queue.txt', 'r+')
repos = inputFile.read().strip().split('\n')
inputFile.truncate(0)
inputFile.close()

for repo in repos: 
	#update local repo from it's source
	g = git.cmd.Git('/home/pi/gitprojects/%s' % repo)
	g.pull()

	g.push('git@github.com:tuffing/%s.git' % repo)
