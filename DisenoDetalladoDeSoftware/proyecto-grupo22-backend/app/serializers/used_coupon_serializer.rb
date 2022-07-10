class UsedCouponSerializer < ActiveModel::Serializer
  include JSONAPI::Serializer
  set_key_transform :camel_lower

  attributes :id, :shopping_cart_id
  
  attribute :name do |used_coupon|
    @coupon = Coupon.find(used_coupon.coupon_id)
    @coupon.name
  end

  attribute :value do |used_coupon|
    @coupon.value
  end

  attribute :category do |used_coupon|
    Category.find(@coupon.category_id).name
  end
end
