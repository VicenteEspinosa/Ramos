# frozen_string_literal: true

require 'rails_helper'

RSpec.describe ProductsController, type: :controller do

  before do
    @food_coupon = FactoryBot.create(:food_coupon)
    @product = FactoryBot.create(:food_product)
  end

  describe "GET /index" do
    it 'find all products' do
      get :index
      expect(response).to have_http_status(200)
    end
  end
end