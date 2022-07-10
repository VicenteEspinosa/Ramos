# frozen_string_literal: true

require 'rails_helper'

RSpec.describe CartItemsController, type: :controller do

  before do
    @cart = FactoryBot.create(:cart_with_user)
    @product = FactoryBot.create(:food_product)
    @cart_item = FactoryBot.create(:food_cart_item)
    @user = FactoryBot.create(:user_with_shopping_cart)
    @cart_with_item = FactoryBot.create(:cart_with_item)
  end

  describe 'post /create' do
    it 'can not create cart item because miss the shoppingcart or the item' do
      post :create, params: { user_id: @user.id, cart_item: { product_id: @product, quantity: -1234 } }
      expect(response).to have_http_status(400)
    end
    it 'return create success' do
      post :create, params: { 
        cart_item: { 
          product_id: @cart_item.product_id, 
          quantity: 10
          },
          user_id: @user.id
        } 
      expect(response).to have_http_status(201)
    end

    it 'return create success' do
      item = CartItem.find_by(shopping_cart_id: @cart_with_item.id)
      item.quantity = 1
      post :create, params: { 
        cart_item: { 
          product_id: item.product_id, 
          quantity: 10
          },
          user_id: @cart_with_item.user_id
        } 
      expect(response).to have_http_status(201)
    end
  end

  describe 'put /update' do
    it 'update successfuly' do
      put :update, params: { 
        cart_item: { 
          product_id: @cart_item.product_id, 
          quantity: 10, 
          shopping_cart_id:@cart_item.shopping_cart_id },
           id: @cart_item.id }
      expect(response).to have_http_status(200)
    end
    it 'can not update' do
      put :update, params: { 
        cart_item: { 
          product_id: @cart_item.product_id, 
          quantity: -1, 
          shopping_cart_id: @cart_item.shopping_cart_id },
           id: @cart_item.id }
      expect(response).to have_http_status(400)
    end
  end

  describe 'DELETE /destroy' do
    it 'destroy successfuly' do
      delete :destroy, params: { id: @cart_item.id}
      expect(response).to have_http_status(200)
    end
  end
end