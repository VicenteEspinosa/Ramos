class ProductsController < ApplicationController

  def index
    render json: ProductSerializer.new(
      Product.all,
      { is_collection: true }
    ).serializable_hash
  end
end
