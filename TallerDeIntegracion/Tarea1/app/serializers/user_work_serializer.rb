class UserWorkSerializer < ActiveModel::Serializer
    attributes :id, :job, :salary, :promotion
end