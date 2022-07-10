MAX_FILTERS = 10
FILTERS = ["audit_types", "service_types"]
generic_filters = [f"filter_{x + len(FILTERS) + 1}" for x in range(MAX_FILTERS - len(FILTERS))]
FILTERS = FILTERS + generic_filters
