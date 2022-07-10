# frozen_string_literal: true

require 'rails_helper'

RSpec.describe CategoriesController, type: :controller do

  describe "GET /index" do
    it 'return http success' do
      get :index
      expect(response).to have_http_status(200)
    end
  end

  describe "POST /create" do
    it 'create category successfully' do
      post :create, params: {category: {name: "game"}}
      expect(response).to have_http_status(201)
    end
    it 'can not create category' do
      post :create, params: {category: {name: ""}}
      expect(response).to have_http_status(400)
    end
  end

  describe "DELETE /destroy" do
    before do
      @category = FactoryBot.create(:food_category)
    end
    it 'delete category successfully' do
      delete :destroy, params: {id: @category.id}
      expect(response).to have_http_status(200)
    end
  end
end