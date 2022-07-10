class UserMedicalSerializer < ActiveModel::Serializer
    attributes :id, :hospital, :operations, :medical_debt
end