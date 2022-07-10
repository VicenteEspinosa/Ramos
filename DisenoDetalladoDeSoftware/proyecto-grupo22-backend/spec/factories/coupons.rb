FactoryBot.define do
  factory :food_coupon, class: Coupon do
    name { "fisrt cuopon" }
    value { 0.2 }
    category_id { FactoryBot.create(:food_category).id }
  end
end