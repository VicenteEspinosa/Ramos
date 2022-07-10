class CartItemsController < ApplicationController
  before_action :set_cart_item, only: %i[ show edit update destroy ]

  def create
    shopping_cart = ShoppingCart.find_by(user_id: params[:user_id], active: true) || ShoppingCart.create!(user_id: params[:user_id], active: true)
    if shopping_cart&.cart_items&.pluck(:product_id)&.include?(cart_item_params[:product_id].to_i)
      cart_item = CartItem.find_by(product_id: cart_item_params[:product_id], shopping_cart_id: shopping_cart.id)
      cart_item.update(quantity: cart_item.quantity + cart_item_params[:quantity].to_i)
    else
      cart_item = CartItem.create(
        product_id: cart_item_params[:product_id],
        shopping_cart_id: shopping_cart.id,
        quantity: cart_item_params[:quantity]
      )
    end

    if cart_item.save
      render json: {data: "Artículo agregado correctamente"}, status: 201
    else
      render json: {data: "No se pudo agregar el producto"}, status: 400
    end
  end

  def update
    update = cart_item_params
    if @cart_item.update({quantity: update[:quantity]})
      render json: {data: "Artículo actualizado correctamente"}, status: 200
    else
      render json: {data: "No se pudo actualizar el artículo"}, status: 400
    end
  end

  def destroy
    @cart_item.destroy
    render json: {data: "Artículo borrado"}, status: 200
  end

  private

    def set_cart_item
      @cart_item = CartItem.find(params[:id])
    end

    def cart_item_params
      params.require(:cart_item).permit(:product_id, :quantity)
    end
end
