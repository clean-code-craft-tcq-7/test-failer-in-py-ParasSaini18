alert_failure_count = 0

def network_alert_stub(celcius):
    if celcius <= 200:
        return 200
    else:
        return 500
    
def network_alert_real(celcius):
    if celcius <= 200:
        return 200
    else:
        return 500
      
def function_pointer(fptr, celcius):
    if fptr == 0:
        return network_alert_stub(celcius)
    else:
        return network_alert_real(celcius)
        
def alert_in_celcius(fptr, farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = function_pointer(fptr, celcius)
    
    if returnCode != 200:
        global alert_failure_count
        alert_failure_count += 1