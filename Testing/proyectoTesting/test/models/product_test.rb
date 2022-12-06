require 'test_helper'

class ProductTest < ActiveSupport::TestCase
  def teardown
    Product.destroy_all
  end

  test 'Product con parametros validos' do
    product = Product.create(name: 'Bebida', category: 'Bebestible', price: 3500, amount: 500)
    assert_equal(true, product.valid?)
  end
end
