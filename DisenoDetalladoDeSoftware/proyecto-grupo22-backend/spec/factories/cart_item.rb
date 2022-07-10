FactoryBot.define do
  factory :food_cart_item, class: CartItem do
    product_id { FactoryBot.create(:food_product).id }
    shopping_cart_id { FactoryBot.create(:cart_with_user).id }
    quantity { 1000 }
  end

  factory :food_cart_item_with_user, class: CartItem do
    product factory: :product
    shoppong_cart factory: :cart_empy
    quantity {10}
  end

  factory :food_cart_item_nil, class: CartItem do
    product_id { FactoryBot.create(:food_product).id }
    shopping_cart_id { nil }
    quantity { 1000 }
  end
end