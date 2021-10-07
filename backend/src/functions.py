import requests, pprint
from src.db import DB_get


DBG = DB_get()


def free(obj):
    panels = DBG.get_panels_data()
    min_panel = []
    for name, cost, power, eff, img, link, producer in panels:
        min_panel.append([
    ((obj["energy"] * obj["stock_value"]) // (power / 1000 * 5) + 1) * cost, name, cost, power, eff, img, link, producer
            ])
    min_panel.sort(key=lambda x:x[0])
    return min_panel[0]
        
def pro(obj):
    insolation, min_insolation, angel = nasa_data(map(float, obj['coords'].split(','))) 
    panels = DBG.get_complects_data()
    min_panel = []
    for name, cost, power, year_power, eff, square, img_link, producer, product, typ in panels:
        p_eff = 0.19
        ins = (min_insolation / 1000 * 24)
        gloabal_cost = cost * int(obj["energy"] * obj["stock_value"] / ((ins * p_eff) * 1.996 * 1.002))
        min_panel.append([
                gloabal_cost, name, cost, power, year_power, eff, square, img_link, producer, product, typ
            ])
    min_panel.sort(key=lambda x:x[0])
    return [insolation, min_panel[0], angel]


def nasa_data(coords):
    lat, lon = coords
    API_URL = ("https://power.larc.nasa.gov/api/temporal/climatology/point"
    "?parameters=SI_EF_TILTED_SURFACE&community=SB&"
    f"longitude={lon}&latitude={lat}&format=JSON&start=2016&end=2017")
    r = requests.get(API_URL)
    ALL_PARAMETERS = r.json()['properties']['parameter']
    insolation = ALL_PARAMETERS['SI_EF_TILTED_SURFACE_OPTIMAL']
    angel = ALL_PARAMETERS['SI_EF_TILTED_SURFACE_OPTIMAL_ANG']
    min_ins = 999999
    for mounth in insolation:
        if mounth == "ANN":
            continue
        ins = insolation[mounth] / 1000 * 24
        min_ins = ins if ins < min_ins else min_ins
        insolation[mounth] = ins
    return insolation, min_ins, angel