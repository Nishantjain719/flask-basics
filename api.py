# in json format its easy to access specific response form that api response
# Api gets information, but we donn't need to know that how? we just need to know
# what request to make in order to get that info and Api handle the rest and use that info and represnet in output.

from flask import Flask, render_template, request, jsonify
@app.route("/api/flights/<int:flght_id>")
def flight_api(flight_api):
    flight = Flight.query.get(flight_id)
    if flight is None:
        # jsonify takes in python dictionaries and convert to json obj(built in in falsk)
        return jsonify({"error": "Invalid flight_id"}), 422

    # Get passengers
    passengers = flight.passengers # due to relationship syntax
    names = []
    for passenger in passengers:
        names.append(passenger.name)
    return jsonify({
        "origin": flight.origin,
        "destination": flight.destination,
        "passengers": names
    })

# its now machine readable in json format and some other developers can talk to our own Api.   
