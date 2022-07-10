class Product < ApplicationRecord
  has_one :category
  has_many :cart_items
end
