FactoryBot.define do
  factory :cart_empy, class: ShoppingCart do
    user_id {nil}
  end

  factory :cart_with_user, class: ShoppingCart do
    user_id {FactoryBot.create(:normal).id}
  end

  factory :past_cart, class: ShoppingCart do
    user factory: :user_with_cart
    payment_date { Time.now }
  end

  factory :cart_with_item, class: ShoppingCart do
    user_id { FactoryBot.create(:normal).id }
    after(:create) do |cart|
      item = FactoryBot.create(:food_cart_item, shopping_cart_id: cart.id)
    end
  end

  factory :cart_with_coupon, class: ShoppingCart do
    user factory: :user_with_shopping_cart
    coupon_id { FactoryBot.create(:food_coupon) }
    payment_date { Time.now }
  end
end