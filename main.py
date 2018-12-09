from flask import Flask, request
from ipaddress import IPv4Address, IPv4Network

app = Flask(__name__)

app.config.from_envvar('WEBHOOK_SETTINGS')

@app.route('/')
def index():
	return 'Tuffing web hooks'

@app.route('/gitpush/<repo>', methods=['GET', 'POST'])
def gitpush(repo):
	valid = False
	
	for ranges in app.config['WHITELIST']:
		if IPv4Address(request.environ.get('HTTP_X_REAL_IP', request.remote_addr)) in IPv4Network(ranges):
			valid = True

	if not valid:
		return 'invalid ip'

	if repo not in app.config['REPOS']:
		return 'no such repo'

	with open("queue.txt", "a") as queue:
	    queue.write('%s\n' % repo)
	queue.close()


	return app.config['GITURL'] % repo
