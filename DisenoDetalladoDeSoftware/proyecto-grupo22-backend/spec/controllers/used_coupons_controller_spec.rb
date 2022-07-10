# frozen_string_literal: true

require 'rails_helper'

RSpec.describe UsedCouponsController, type: :controller do

  before do
    @cart = FactoryBot.create(:cart_with_user)
    @coupon = FactoryBot.create(:food_coupon)
    @used_coupon = UsedCoupon.create({coupon_id: @coupon.id, shopping_cart_id: @cart.id})
    @used_coupon.save
  end

  describe "GET /index" do
    it 'find all used coupons' do
      get :index
      expect(response).to have_http_status(200)
    end
  end

end