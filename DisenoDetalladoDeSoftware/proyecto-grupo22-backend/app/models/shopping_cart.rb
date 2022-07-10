class ShoppingCart < ApplicationRecord
  belongs_to :user
  has_one :coupon
  has_many :cart_items
end
