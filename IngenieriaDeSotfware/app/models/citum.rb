class Citum < ApplicationRecord
  belongs_to :dater, :class_name => 'User', foreign_key: 'user_id'
  belongs_to :dated, :class_name => 'User', foreign_key: 'user_2_id'
  belongs_to :restaurant
end
