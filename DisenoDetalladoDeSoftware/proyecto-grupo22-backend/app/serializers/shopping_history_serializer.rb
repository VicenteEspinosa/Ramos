class ShoppingHistorySerializer < ActiveModel::Serializer
  include JSONAPI::Serializer
  set_key_transform :camel_lower

  attributes :id, :payment_date, :total_amount

  attribute :coupon do |shopping_cart|
    @coupon = Coupon.find_by(id: shopping_cart.coupon_id)
    @coupon.name if @coupon
  end

  attribute :discount do |shopping_cart|
    if @coupon
      if shopping_cart.total_amount < @coupon.value
        shopping_cart.total_amount 
      else
        @coupon.value
      end
    end
  end

  attribute :items do |shopping_cart|
    shopping_cart.cart_items.map do |cart_item|
      {
        id: cart_item.product_id,
        name: cart_item.product.name,
        price: cart_item.product.price,
        quantity: cart_item.quantity
      }
    end
  end
end