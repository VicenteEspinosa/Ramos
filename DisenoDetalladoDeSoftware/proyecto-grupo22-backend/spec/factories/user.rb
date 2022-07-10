# frozen_string_literal: true

FactoryBot.define do
  sequence :email do |n|
    "person#{n}@example.com"
  end

  factory :admin, class: :User do
    created_at { 1_557_933_657 }
    updated_at { 1_557_933_657 }
    email
    password { 123_456 }
    password_confirmation { 123_456 }
  end

  factory :normal , class: :User do
    created_at { 1_557_933_657 }
    updated_at { 1_557_933_657 }
    email
    password { 123_456 }
    password_confirmation { 123_456 }
  end

  factory :user_with_shopping_cart, class: :User do 
    created_at { 1_557_933_657 }
    updated_at { 1_557_933_657 }
    email
    password { 123_456 }
    password_confirmation { 123_456 }
    after(:create) do |user_with_cart|
      FactoryBot.create(:cart_empy, user_id: user_with_cart.id)
      FactoryBot.create(:past_cart, user_id: user_with_cart.id)
      FactoryBot.create(:past_cart, user_id: user_with_cart.id)
      user_with_cart.reload
    end
  end

  factory :user_with_item_cart, class: :User do 
    created_at { 1_557_933_657 }
    updated_at { 1_557_933_657 }
    email
    password { 123_456 }
    password_confirmation { 123_456 }
    after(:create) do |user_with_cart|
      cart = ShoppingCart.create({user_id: user_with_cart.id})
      cart.save
      category = FactoryBot.create(:food_category)
      product = Product.create({name: "milk", price: 1234, category_id: category.id})
      product.save
      CartItem.create({product_id: product.id, shopping_cart_id: cart.id})
      user_with_cart.reload
    end
  end
end