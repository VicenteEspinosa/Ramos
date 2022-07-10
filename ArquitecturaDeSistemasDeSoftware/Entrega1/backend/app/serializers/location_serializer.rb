class LocationSerializer < ActiveModel::Serializer
  attributes :id, :lat, :long, :name

  has_one :user
end
