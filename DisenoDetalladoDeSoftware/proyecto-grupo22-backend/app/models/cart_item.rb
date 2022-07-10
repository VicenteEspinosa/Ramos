class CartItem < ApplicationRecord
  belongs_to :product, foreign_key: "product_id"
  belongs_to :shopping_cart, foreign_key: "shopping_cart_id"

  validates :quantity, numericality: { greater_than_or_equal_to: 0 }
end
