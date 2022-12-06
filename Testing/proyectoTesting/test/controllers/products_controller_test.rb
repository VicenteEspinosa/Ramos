require 'test_helper'

class ProductsControllerTest < ActionDispatch::IntegrationTest
  def setup
    @product = Product.create!(name: 'test product', price: 10, category: 'Comestibles', amount: 10)
  end

  def teardown
    Reserva.destroy_all
  end

  test 'should get index' do
    get '/products'
    assert_response :success
  end

  test 'should create product' do
    assert_difference('Product.count') do
      post '/products', params:
      {
        product:
        {
          amount: @product.amount,
          category: @product.category,
          name: @product.name,
          price: @product.price
        }
      }
    end

    assert_redirected_to products_url(Product.last)
  end

  test 'should show product' do
    get "/products/#{@product.id}"
    assert_response :success
  end

  test 'should update product' do
    patch "/products/#{@product.id}", params:
    {
      product:
      {
        amount: @product.amount,
        category: @product.category,
        name: @product.name,
        price: @product.price
      }
    }
    assert_redirected_to products_url(@product)
  end

  test 'DELETE product' do
    delete "/products/#{@product.id}"
    assert_response :success
  end

  test 'should filter by category' do
    get "/products/#{@product.category}/category"
    assert_response :success
  end

  test 'should fail create product' do
    post '/products', params:
    {
      product:
      {
        amount: @product.amount,
        category: 'invalid category',
        name: @product.name,
        price: @product.price
      }
    }
    assert_response :unprocessable_entity
  end

  test 'should fail update product' do
    patch "/products/#{@product.id}", params:
    {
      product:
      {
        category: 'invalid category'
      }
    }
    assert_equal(flash[:notice], 'Error while updating.')
  end
end
