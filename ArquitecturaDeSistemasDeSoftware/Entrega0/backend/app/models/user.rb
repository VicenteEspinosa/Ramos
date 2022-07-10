class User < ApplicationRecord
  has_many :location
  has_many :sent_pings, class_name: 'Ping', foreign_key: 'sender_id'
  has_many :received_pings, class_name: 'Ping', foreign_key: 'receiver_id'
end
