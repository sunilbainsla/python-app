#!flask/bin/python
from flask import Flask, jsonify,abort,make_response
from flask_httpauth import HTTPBasicAuth
app = Flask(__name__)
auth = HTTPBasicAuth()
supply = [
   	{
		"Field Name": "name",
		"Category": "Personal",
		"Sec Type": "Confidential",
		"Colomn": "name"
	},
	{
		"Field Name": "add1",
		"Category": "Personal",
		"Sec Type": "Confidential",
		"Colomn": "add1"
	},
	{
		"Field Name": "add2",
		"Category": "Personal",
		"Sec Type": "Confidential",
		"Colomn": "add2"
	},
	{
		"Field Name": "add3",
		"Category": "Personal",
		"Sec Type": "Confidential",
		"Colomn": "add3"
	},
	{
		"Field Name": "gender",
		"Category": "Personal",
		"Sec Type": "Confidential",
		"Colomn": "gender"
	},{
		"Field Name": "add2",
		"Category": "Contract",
		"Sec Type": "Confidential",
		"Colomn": "add2"
	},
	{
		"Field Name": "add3",
		"Category": "Contract",
		"Sec Type": "Confidential",
		"Colomn": "add3"
	},
	{
		"Field Name": "gender",
		"Category": "Contract",
		"Sec Type": "Confidential",
		"Colomn": "gender"
	}
]

@app.route('/api/connectfore/v1/supplys/<sectype>', methods=['GET'])
@auth.login_required
def get_supply(sectype):
    sup = [sup for sup in supply if sup['Category'] == sectype]
    if len(sup) == 0:
        abort(404)
    return jsonify({'supply': sup})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@auth.get_password
def get_password(username):
    if username == 'sunil':
        return 'sunil'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')