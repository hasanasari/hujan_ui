import json
from django.conf import settings
from .utils import MAAS


def get_machines(machine_id=None):
    if settings.WITH_EX_RESPONSE:
        with open(settings.DIR_EX_RESPONSE + "machines.json") as readfile:
            machines = json.load(readfile)
    else:
        maas = MAAS()
        machines = maas.get("machines/").json()
        machine_file = open("hujan_ui/maas/ex_response/machines.json", "w")
        json.dump(machines, machine_file)
        machine_file.close()

    return machines


def get_subnets(subnet_id=None):
    if  settings.WITH_EX_RESPONSE:
        with open(settings.DIR_EX_RESPONSE + "subnets.json") as readfile:
            subnets = json.load(readfile)
        if subnet_id:
            sub = [subnet for subnet in subnets if subnet['id'] == subnet_id]
            subnets = sub[0] if sub else []
            
    else:
        maas = MAAS()
        if subnet_id:
            subnets = maas.get("subnets/{subnet_id}/").json()
        else:
            subnets = maas.get("subnets/").json()
            subnet_file = open('hujan_ui/maas/ex_response/subnets.json','w')
            json.dump(subnets,subnet_file)
            subnet_file.close()
    return subnets


def get_fabrics(fabric_id=None):
    if  settings.WITH_EX_RESPONSE:
        with open(settings.DIR_EX_RESPONSE + "fabrics.json") as readfile:
            fabrics = json.load(readfile)
        if fabric_id:
            fab = [f for f in fabrics if f['id'] == fabric_id]
            fabrics = fab[0] if fab else []
        vlans = load_dokumen('vlans.json')
        store = []
        for f in fabrics:
            for g in f['vlans']:
                store.append(g)
        write_dokumen(store, 'vlans.json')

            
    else:
        maas = MAAS()
        if fabric_id:
            fabrics = maas.get(f"fabrics/{fabric_id}/").json()
        else:
            fabrics = maas.get("fabrics/").json()
            fabric_file = open('hujan_ui/maas/ex_response/fabrics.json','w')
            json.dump(fabrics, fabric_file)
            fabric_file.close()
            
    return fabrics
    

def get_spaces(space_id=None):
    if settings.WITH_EX_RESPONSE:
        with open(settings.DIR_EX_RESPONSE + "spaces.json") as readfile:
            spaces = json.load(readfile)
        if space_id:
            s = [space for space in spaces if space['id'] == space_id]
            spaces = s[0] if s else []

    else:
        m = MAAS()
        if space_id:
            spaces = m.get('spaces/{space_id}/').json()
        else:
            spaces = m.get('spaces/').json()
            space_file = open('hujan_ui/maas/ex_response/spaces.json','w')
            json.dump(spaces, space_file)
            space_file.close()

    return spaces


def get_vlans(id=None):
    vlans = []
    with open(settings.DIR_EX_RESPONSE + "vlans.json") as readfile:
        vlans =json.load(readfile)
    if not vlans:
        vlans = []
    else:
        if id:
            vlan = [i for i in vlans if i['id'] == id]
            vlans = vlan[0] if vlan else []
    return vlans


def load_dokumen(data):
    with open(settings.DIR_EX_RESPONSE + data) as readfile:
        res = json.load(readfile)
    return res


def write_dokumen(data, store):
    file = open(settings.DIR_EX_RESPONSE + store, 'w')
    json.dump(data, file)
    file.close()
        