class Match < ApplicationRecord
  belongs_to :matcher, :class_name => 'User', foreign_key: 'user_id'
  belongs_to :matched, :class_name => 'User', foreign_key: 'user_2_id'
end
