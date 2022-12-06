# Controlador de productos
class ProductsController < ApplicationController
  skip_before_action :verify_authenticity_token
  protect_from_forgery with: :null_session
  before_action :set_product, only: %i[show update destroy]

  # GET /products or /products.json
  def index
    @products = Product.all

    render json: @products
  end

  # GET /products/1 or /products/1.json
  def show
    render json: @product
  end

  def filter_by_category
    @products = Product.where(category: params[:category])

    render json: @products
  end

  # POST /products or /products.json
  def create
    @product = Product.new(product_params)

    respond_to do |format|
      if @product.save
        format.html do
          redirect_to products_url(@product), notice: 'Product was successfully created.'
        end
        format.json { render :show, status: :created, location: @product }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @product.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /products/1 or /products/1.json
  def update
    respond_to do |format|
      if @product.update(product_params)
        format.html do
          redirect_to products_url(@product), notice: 'Product was successfully updated.'
        end
        format.json { render :show, status: :ok, location: @product }
      else
        format.html do
          redirect_to products_url(@product), notice: 'Error while updating.'
        end
        format.json { render json: @product.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /products/1 or /products/1.json
  def destroy
    @product.destroy
  end

  private

  # Use callbacks to share common setup or constraints between actions.
  def set_product
    @product = Product.find(params[:id])
  end

  # Only allow a list of trusted parameters through.
  def product_params
    params.require(:product).permit(:price, :category, :amount, :name)
  end
end
