import pazfit_utils
import os
from eve import Eve
from flask import url_for, render_template, g
app = Eve(settings=os.path.join(os.path.dirname(__file__), 'settings.py'))


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/sheet')
def sheet():
	print g
	values = {"version": 0}
	return render_template('sheet/index.html')

@app.route('/sheet/<name>')
def sheet_index(name):
	return render_template('sheet/{0}.html'.format(name))


@app.context_processor
def inject_environment():
    return {
		"version": 0
	}


class HooksRegistar():
	def __init__(self, eveApp):
		app.on_replace_log += self.on_replace_log
		app.on_update_log += self.on_update_log
		app.on_replace_max += self.on_replace_max
		app.on_insert_log += self.on_insert_log

	def on_insert_log(self, items):
		for log in items:
			self.on_replace_log(log, None)

	def on_update_log(self, updates, original):
		self.on_replace_log(updates, origina)

	def on_replace_log(self, updates, original):
		maxes = app.data.driver.db['max']
		effective_max = maxes.find({"date": {"$lte": updates["date"] }})[0]
		self.log_do_calculations(updates, effective_max)

	def on_replace_max(self, updates, original):
		log_collection = app.data.driver.db['log']
		print log_collection

		affected_logs = log_collection.find({"date": {"$gte": updates["date"] }})

		for l in affected_logs:
			r = self.log_do_calculations(l, updates)
			log_collection.save(l)

	def log_do_calculations(self, log, effective_max=None):
		if effective_max is None:
			maxes = app.data.driver.db['max']
			effective_max = maxes.find({"date": {"$lte": updates["date"] }})[0]

		max_weight = effective_max[log["lift"]]

		log["calculated"] = {
			"effectiveMax": max_weight,
			"estimatedMax": log["weight"]*log["reps"]*0.0333 + log["weight"],
			"targetMax": int(round(37-36*log["weight"]/max_weight+5)),
		}

		return log



HooksRegistar(app)

if __name__ == '__main__':
	    app.run()


