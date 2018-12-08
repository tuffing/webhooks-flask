from flask import Flask, request
import git
app = Flask(__name__)
#app.config.from_object('yourapplication.default_settings')

app.config.from_envvar('WEBHOOK_SETTINGS')

@app.route('/')
def index():
    return 'Tuffing web hooks'

@app.route('/gitpush/<repo>', methods=['GET', 'POST'])
def gitpush(repo):
	#return '%s gitpush' % repo
	#return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
	if request.environ.get('HTTP_X_REAL_IP', request.remote_addr) not in app.config['WHITELIST']:
		return 'invalid ip'

	if repo not in app.config['REPOS']:
		return 'no such repo'

	#update local repo from it's source
	g = git.cmd.Git(app.config['GITPATH'] % repo)
	g.pull()

	g.push(app.config['GITURL'] % repo)

	return app.config['GITURL'] % repo