def calculate_flight_time(weight_grams):
    #for this description I had to edit the comment because it did not provide the """ at the end of the comment so the whole code became a comment."
    """Calculates the flight time of a drone based on the payload weight."""
    # All I had to type was if and and it finished the whole statement for me exactly the way I wanted it
    if weight_grams < 0:
        raise ValueError("Payload weight must be non-negative.")

    #I had to reject copilot here because it was attempting to use flight time not flight_time whis was not recognized. 
    flight_time = 180 - 0.1 * weight_grams
    return max(0.0, flight_time)


def flight_time_table(max_weight_grams, step_grams):
    """Generates a table of flight times for different payload weights."""
    table = []
    weight = 0
    while weight <= max_weight_grams:
        time_val = calculate_flight_time(weight)
        table.append((weight, time_val))
        weight += step_grams
    return table