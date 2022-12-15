import alerter

def test_alert_in_celcius():
    alerter.alert_in_celcius(0, 303.6)
    assert(alerter.alert_failure_count == 0)
    alerter.alert_in_celcius(0, 450)
    assert(alerter.alert_failure_count == 1)
    alerter.alert_in_celcius(0, 100)
    assert(alerter.alert_failure_count == 1)
    alerter.alert_in_celcius(0, 500)
    assert(alerter.alert_failure_count == 2)
    
if __name__ == '__main__':
    test_alert_in_celcius()

print("All is well (maybe!)\n")