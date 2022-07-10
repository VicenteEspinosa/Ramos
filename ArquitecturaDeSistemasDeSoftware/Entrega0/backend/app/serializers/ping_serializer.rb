class PingSerializer < ActiveModel::Serializer
  attributes :id, :created_at, :updated_at

  has_one :sender
  has_one :receiver
end
