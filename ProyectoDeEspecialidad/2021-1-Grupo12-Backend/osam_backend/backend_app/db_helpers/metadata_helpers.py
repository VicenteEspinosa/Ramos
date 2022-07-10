from backend_app.db_models.metadata import Metadata


def get_metadata_header(metadata_ids):
    """Returns the metadata header for the report."""

    metadata_header = []
    for metadata_id in metadata_ids:
        try:
            metadata_header.append(Metadata.objects.get(id=metadata_id).name)
        except Metadata.DoesNotExist:
            metadata_header.append("ERROR")

    return metadata_header


def get_metadata_ids(report):
    """Returns the metadata ids for the report."""

    category = "1" if report.category == "1" else "0"
    metadata_ids = [metadata.id for metadata in Metadata.objects.all() if category in metadata.category["category_ids"]]
    return metadata_ids
