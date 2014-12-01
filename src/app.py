import pazfit_utils
import os
from eve import Eve
from flask import url_for, render_template, g
SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py')
app = Eve(settings=SETTINGS_PATH)

def calc_repgoal(weight, max_weight):
    return int(round(37-36*weight/max_weight+5))

def calc_estimated_max(weight, reps):
    return weight*reps*0.0333+weight

def calc_target_max(weight, max_weight):
    return calc_estimated_max(weight, calc_repgoal(weight, max_weight))

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
        effective_max = self.log_find_effective_max(updates)
        self.log_do_calculations(updates, effective_max)

    def on_replace_max(self, updates, original):
        log_collection = app.data.driver.db['log']
        print log_collection

        affected_logs = log_collection.find({"date": {"$gte": updates["date"] }})

        for l in affected_logs:
            r = self.log_do_calculations(l)
            log_collection.save(l)

    def log_find_effective_max(self, log):
        maxes = app.data.driver.db['max']
        effective_max = maxes.find({"date": {"$lte": log["date"] }}).sort('date',-1)[0]
        return effective_max


    def log_do_calculations(self, log, effective_max=None):
        print 'lolwtf4'
        if effective_max is None:
            effective_max = self.log_find_effective_max(log) 

        max_weight = effective_max[log["lift"]]

        log["calculated"] = {
                "effectiveMax": max_weight,
                "estimatedMax": calc_estimated_max(log["weight"],log["reps"]),
                "targetMax": calc_target_max(log["weight"], max_weight),
                "repgoal": calc_repgoal(log["weight"],max_weight),
                }

        print log["calculated"]

        return log



HooksRegistar(app)

if __name__ == '__main__':
    app.run(host=os.environ.get('PAZFIT2_SERVICES_BIND','0.0.0.0'))


