# frozen_string_literal: true

require 'rails_helper'

RSpec.describe CouponsController, type: :controller do

  before do
    @coupon = FactoryBot.create(:food_coupon)
  end
  describe 'GET /index' do
    it 'return http success' do
      get :index
      expect(response).to have_http_status(200)
    end
  end

  describe 'POST /create' do
    it 'create coupon successfully' do
      post :create, params: { 
        coupon: { 
          name: @coupon.name, 
          value: @coupon.value, 
          category_id: @coupon.category_id 
          }
        } 
        expect(response).to have_http_status(302)
    end

    it 'can not create, because value is negative' do
      post :create, params: { 
        coupon: { 
          name: @coupon.name, 
          value: -1, 
          category_id: @coupon.category_id 
          }
        } 
        expect(response).to have_http_status(422)
    end
  end

  describe 'PUT /update' do
    it 'update coupon successfully' do
      put :update, params: { 
        coupon: { 
          name: @coupon.name, 
          value: @coupon.value, 
          category_id: @coupon.category_id 
          },
          id: @coupon.id 
        } 
        expect(response).to have_http_status(302)
    end

    it 'can not update, because value is negative' do
      put :update, params: { 
        coupon: { 
          name: @coupon.name, 
          value: -1, 
          category_id: @coupon.category_id 
          },
          id: @coupon.id 
        } 
        expect(response).to have_http_status(422)
    end
  end

  describe 'DELETE /destroy' do
    it 'delete coupont success' do
      delete :destroy, params: { id: @coupon.id }
      expect(response).to have_http_status(302)
    end
  end

  describe 'POST /verify' do
    it 'verificate the coupon' do
      post :verify, params: { code: @coupon.name }
      expect(response).to have_http_status(200)
    end

    it 'can not verificate the coupon' do
      post :verify, params: { code: "MALO" }
      expect(response).to have_http_status(400)
    end
  end
end