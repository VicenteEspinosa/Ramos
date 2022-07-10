# frozen_string_literal: true

require 'rails_helper'

RSpec.describe ShoppingCartsController, type: :controller do

  before do
    @user = FactoryBot.create(:normal)
    @user_with_cart = FactoryBot.create(:user_with_shopping_cart)
    @food_coupon = FactoryBot.create(:food_coupon)
    @cart = ShoppingCart.find_by(user_id: @user_with_cart.id)
    @cart_item = FactoryBot.create(:food_cart_item)
    @user_cart_item = FactoryBot.create(:user_with_item_cart)
    @cart_with_coupon = FactoryBot.create(:cart_with_coupon)
  end

  describe 'post /create' do
    
    it 'returns http 201' do
      post :create, params: { id: @user.id} 
      expect(response).to have_http_status(201)
    end
    it 'cannot create a shopping cart, becuase miss the user' do
      post :create, params: { id: -1} 
      expect(response).to have_http_status(400)
    end
  end

  describe 'GET /show' do
    it 'return http success' do
      get :show, params: {id: @user_with_cart.id}
      expect(response).to have_http_status(200)
    end
  end

  describe 'PUT /update' do
    it 'return update correct' do
      cart = ShoppingCart.find_by(user_id: @user_with_cart.id, payment_date: nil)
      put :update, params: {id: cart.id, coupon_id: @food_coupon.id}
      expect(response).to have_http_status(200)
    end

    it 'return update correct' do
      cart = ShoppingCart.find_by(user_id: @user_with_cart.id, payment_date: nil)
      put :update, params: {id: -1, coupon_id: @food_coupon.id, user_id: @user_with_cart.id}
      expect(response).to have_http_status(200)
    end
  end

  describe 'DEL /destroy' do
    it 'return destroy correct' do
      delete :destroy, params: {id: @cart.id}
      expect(response).to have_http_status(200)
    end
  end

  describe 'GET /shopping_history' do
    it 'return http 200' do
      get :shopping_history, params: {id: @user_with_cart.id}
      expect(response).to have_http_status(200)
    end
  end

  # describe 'POST /pay_cart' do
  #   it 'pay successfully' do
  #     cart = ShoppingCart.find_by(user_id: @user_cart_item.id)
  #     item_products = CartItem.where(shopping_cart_id: cart.id).first
  #     puts item_products
  #     product = Product.find(item_products.product_id)
  #     post :pay_cart, params: {id: @user_cart_item.id, data: { total: 3000, products: [product] }, }
  #     expect(response).to have_http_status(201)
  #   end
  # end
end