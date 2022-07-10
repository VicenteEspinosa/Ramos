from backend_app.db_models.commune import Commune
from backend_app.db_models.province import Province
from backend_app.db_models.region import Region
from backend_app.db_models.att_zone import AttZone
from backend_app.db_models.crmzone import CrmZone


def get_location(commune_id, location_data):
    """Gets the commune, province and region."""

    commune = Commune.objects.get(id=commune_id)
    if commune:
        province = get_province(commune.province_id)
        region = get_region(province.region_id)
        att_zone = get_att_zone(commune.region_zona_att)
        crmzone = get_crmzone(commune.region_crm)
        location_data["zone_att"] = att_zone
        location_data["zone_crm"] = crmzone 
        location_data["commune"] = commune.name
        location_data["province"] = province.name
        location_data["region"] = region.name
        location_data["street_name"] = location_data["street_name"].upper()
        return location_data


def get_province(province_id):
    """Gets the province this commune belongs to."""

    province = None
    try:
        province = Province.objects.get(id=province_id)
    except Province.DoesNotExist:
        pass
    finally:
        return province


def get_region(region_id):
    """Gets the region this commune belongs to."""

    region = None
    try:
        region = Region.objects.get(id=region_id)
    except Region.DoesNotExist:
        return region
    finally:
        return region


def get_att_zone(region_zona_att):
    """Gets the att zone name."""
    try:
        att_zone = AttZone.objects.get(id=region_zona_att)
        return att_zone.name
    except AttZone.DoesNotExist:
        return None


def get_crmzone(region_crm):
    """Gets the crmzone name"""

    try:
        crmzone = CrmZone.objects.get(id=region_crm)
        return crmzone.name
    except CrmZone.DoesNotExist:
        return None


def check_province_dependencies(province):
    """Checks if province belongs to any commune."""

    allowed_to_delete = True
    commune_dependency_list = []
    communes = Commune.objects.all()
    for commune in communes:
        if province.id == commune.province_id:
            allowed_to_delete = False
            commune_dependency_list.append({"id": commune.id, "name": commune.name})
    return (commune_dependency_list, allowed_to_delete)


def check_region_dependencies(region):
    """Checks if region belongs to any province."""

    allowed_to_delete = True
    province_dependency_list = []
    provinces = Province.objects.all()
    for province in provinces:
        if region.id == province.region_id:
            allowed_to_delete = False
            province_dependency_list.append({"id": province.id, "name": province.name})
    return (province_dependency_list, allowed_to_delete)


def check_att_zone_dependencies(att_zone):
    """Checks if att_zone belong to any commune"""

    communes = Commune.objects.filter(region_zona_att=att_zone.id)
    if len(communes) > 0:
        allowed_to_delete = False
        commune_dependency_list = list(map(lambda c: {"id": c.id, "name": c.name}, communes))
    else:
        allowed_to_delete = True
        commune_dependency_list = []

    return (commune_dependency_list, allowed_to_delete)


def check_crmzone_dependencies(crmzone):
    """Checks if crmzone belongs to any commune"""

    communes = Commune.objects.filter(region_crm=crmzone.id)
    if len(communes) > 0:
        allowed_to_delete = False
        commune_dependency_list = list(map(lambda c: {"id": c.id, "name": c.name}, communes))
    else:
        allowed_to_delete = True
        commune_dependency_list = []

    return (commune_dependency_list, allowed_to_delete)
