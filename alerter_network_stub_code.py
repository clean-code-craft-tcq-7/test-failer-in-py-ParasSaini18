import alerter

def network_alert_stub(celcius):
    if celcius <= 200:
        return None
    alerter.alert_failure_count += 1