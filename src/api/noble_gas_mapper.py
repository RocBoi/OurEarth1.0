NOBLE_GASES = ["He","Ne","Ar","Kr","Xe","Rn"]

def map_gases(dataset):

    gas_data = {}

    for gas in NOBLE_GASES:
        gas_data[gas] = "proxy_estimate"

    return gas_data
