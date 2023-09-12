from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    current_day = datetime.datetime.utcnow().strftime('%A')

    # Get current UTC time with validation of +/-2 minutes
    current_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # GitHub URLs
    github_file_url = 'https://github.com/username/repo/blob/main/file_name.ext'
    github_repo_url = 'https://github.com/username/repo'

    # Prepare JSON response
    response = {
        'slack_name': 'Oladimeji Daniel',
        'current_day': current_day,
        'utc_time': current_time,
        'track': 'backend',
        'github_file_url': 'https://github.com/DanielOladimeji/hngxstageone.git',
        'github_repo_url': 'https://github.com/DanielOladimeji/hngxstageone/repo/blob/main/api.py',
        'status_code': 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
