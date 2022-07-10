class ShoppingCartsController < ApplicationController

  # GET /shopping_carts/1
  def show
    shopping_cart = ShoppingCart.find_by(user_id: params[:id], active: true)
    cart_items = shopping_cart.cart_items
    cart_products = cart_items.map { |item| {product: item.product, quantity: item.quantity, id: item.id} }
    coupon = Coupon.find_by(id: shopping_cart.coupon_id)
    render json: {
      data: cart_products,
      coupon: coupon ?
      {
        name: coupon.name,
        value: coupon.value
      } :
      nil,
    }, status: 200
  end

  # POST /shopping_carts
  def create
    @shopping_cart = ShoppingCart.create(user_id: params[:id])
    if @shopping_cart.save
      render json: {data: "Carrito creado correctamente"}, status: 201
    else
      render json: {data: "No se pudo crear el carrito"}, status: 400
    end
  end

  def update
    if params[:id].to_i == -1
      shopping_cart = ShoppingCart.find_by(user_id: params[:user_id], active: true) # TODO cambiar user
    else
      shopping_cart = ShoppingCart.find(params[:id])
    end
    if shopping_cart.update(coupon_id: params[:coupon_id])
      render json: {data:"Carrito actualizado correctamente"}, status: 200
    else
      render json: {data: "Carrito no se pudo actualizar"}, status: 400
    end
  end

  def destroy
    @shopping_cart = ShoppingCart.find(params[:id])
    @shopping_cart.destroy
    render json: {data: "carrito borrado correctamente"}, status: 200
  end

  def pay_cart
    shopping_cart = ShoppingCart.find_by(user_id: params[:id], active: true)
    @products = params[:data][:products]
    total = params[:data][:total]
    @products.each do |product|
      item = CartItem.find_by(product_id: product["id"], shopping_cart_id: shopping_cart.id)
      item.update(quantity: product["quantity"])
    end
    shopping_cart.update({payment_date: Time.now, active: false, total_amount: total})
    UsedCoupon.create(coupon_id: shopping_cart.coupon_id, shopping_cart_id: shopping_cart.id) if shopping_cart.coupon_id
    ShoppingCart.create(user_id: params[:id])
    render json: {data: "Compra realizada con éxito"}, status: 201
  end

  def shopping_history
    past_purchases = ShoppingCart.where(user_id: params[:id]).where.not(payment_date: nil).order(payment_date: :desc)
    render json: ShoppingHistorySerializer.new(
      past_purchases,
      { is_collection: true }
    ).serializable_hash, status: 200
  end
end
