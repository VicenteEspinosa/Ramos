class UserBasicSerializer < ActiveModel::Serializer
    attributes :id, :username, :name, :age
end