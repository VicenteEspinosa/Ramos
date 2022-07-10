class UserEducationSerializer < ActiveModel::Serializer
    attributes :id, :psu_score, :university, :gpa_score
end