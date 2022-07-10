class Coupon < ApplicationRecord

  validates :value, numericality: { greater_than_or_equal_to: 0 }
end
