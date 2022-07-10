class UnregisteredUserSerializer < ActiveModel::Serializer
    attributes :username, :mail, :contact
  end
  