from backend_app.db_serializers.info_panel_serializer import InfoPanelSerializer
from backend_app.db_models.user import User
import logging

def create_info_data(timestamp, 
                     auditor_id, 
                     technician_id,
                     data_type,
                     answer_id, 
                     photos):
    auditor_name = get_auditor_name(auditor_id)

    infodata = {
                "timestamp": timestamp,
                "auditor_id": auditor_id,
                "technician_id": technician_id,
                "data_type": data_type,
                "auditor_name": auditor_name,
                "answer_id": answer_id,
                "photos": photos }

    infodata_serializer = InfoPanelSerializer(data=infodata)
    if infodata_serializer.is_valid():
        new_infodata =  infodata_serializer.save()
        new_infodata.save()
    else:
        logging.error(f"Info data error data type: {data_type}")


def get_auditor_name(auditor_id):
    auditor = User.objects.get(user_id=auditor_id)
    return auditor.first_name
