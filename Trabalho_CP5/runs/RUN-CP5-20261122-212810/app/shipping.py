"""Parcel classification teaching build T08-B1.0; weights in whole grams."""
def quote(weight, zone, express):
    if type(weight) is not int or weight < 1 or weight >= 20000 or zone not in ("LOCAL", "REMOTE") or type(express) is not bool:
        return {"status":"INVALID","fee":None}
    if zone == "REMOTE" and express and weight > 10000:
        return {"status":"UNAVAILABLE","fee":None}
    if weight < 1000:
        fee = 5
    elif weight <= 5000:
        fee = 8
    else:
        fee = 12
    if zone == "REMOTE":
        fee = 4
    if express:
        fee += 6
    return {"status":"OK","fee":fee}
