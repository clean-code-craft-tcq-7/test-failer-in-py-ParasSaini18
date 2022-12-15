import alerter_network_stub_code

alert_failure_count = 0
    
def network_alert_real(celcius):
    if celcius <= 200:
        return None
    global alert_failure_count
    alert_failure_count += 1
      
def function_pointer(fptr, celcius):
    if fptr == 0:
        return alerter_network_stub_code.network_alert_stub(celcius)
    return network_alert_real(celcius)
        
def alert_in_celcius(fptr, farenheit):
    celcius = (farenheit - 32) * 5 / 9
    function_pointer(fptr, celcius)
