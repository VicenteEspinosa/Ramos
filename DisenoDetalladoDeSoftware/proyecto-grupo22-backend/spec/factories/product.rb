FactoryBot.define do
  factory :food_product, class: Product do
    before(:create) do |coupon|
      category = FactoryBot.create(:food_category)
    end
    name { "milk" }
    price { 1000 }
    category_id {  FactoryBot.create(:food_category).id }
  end
end